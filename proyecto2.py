#Roberta ruvalcaba,Haidany perez,Raquel de leon
import re, math, random, datetime, os, time, unicodedata, urllib.request, json

# ── Soporte Unicode ─────────────────────────────────────────────────────────
try:
    "█▓▒░".encode(os.device_encoding(1) or "utf-8")
    BLOQUE, MEDIO, BAJO, VACIO = "█", "▓", "▒", "░"
except Exception:
    BLOQUE, MEDIO, BAJO, VACIO = "#", "=", "-", "."

PANEL_W, BAR_W = 26, 18

# ── Datos ───────────────────────────────────────────────────────────────────
MATERIAS = [
    "reacciones quimicas", "modulo ofimatica", "ingles 4",
    "conciencia historica", "orientacion", "temas selectos de matematicas 1"
]
AREAS = {
    "reacciones quimicas":             "Ciencias Quimicas / Ing. Quimica",
    "modulo ofimatica":                "Tecnologias de la Informacion",
    "ingles 4":                        "Lenguas / Relaciones Internacionales",
    "conciencia historica":            "Ciencias Sociales / Derecho",
    "orientacion":                     "Psicologia / Desarrollo Humano",
    "temas selectos de matematicas 1": "Ingenieria / Matematicas Aplicadas",
}
NOMBRES = {
    "reacciones quimicas":             "Reacciones Quimicas",
    "modulo ofimatica":                "Modulo Ofimatica",
    "ingles 4":                        "Ingles 4",
    "conciencia historica":            "Conciencia Historica",
    "orientacion":                     "Orientacion",
    "temas selectos de matematicas 1": "Temas Selectos de Matematicas 1",
}
CONSEJOS = [
    "Estudia en bloques de 25 minutos.", "Repasa antes de dormir.",
    "Crea resumenes con tus propias palabras.", "Practica ejercicios pasados.",
]

# ── Auxiliares ───────────────────────────────────────────────────────────────
def normalizar(t):
    t = unicodedata.normalize("NFD", t.strip().lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")

def limpiar():
    try: os.system("cls" if os.name == "nt" else "clear")
    except: print("\n" * 3)

def animacion(msg, seg=2):
    frames, fin, i = ["|", "/", "-", "\\"], time.time() + seg, 0
    while time.time() < fin:
        try: print(f"\r{msg} {frames[i%4]}", end="", flush=True); time.sleep(0.15); i += 1
        except: time.sleep(0.15)
    print("\r" + " " * (len(msg) + 4) + "\r", end="")

def escribir_lento(texto, delay=0.025):
    for c in texto: print(c, end="", flush=True); time.sleep(delay)
    print()

# ── Entradas ─────────────────────────────────────────────────────────────────
def pedir_materia(msg):
    while True:
        m = normalizar(input(msg))
        if re.match(r'^[\w\s]+$', m, re.UNICODE) and m in MATERIAS: return m
        print("Materia no valida. Intenta de nuevo.")

def pedir_dato(msg, tipo, rango):
    while True:
        try:
            v = tipo(input(msg))
            if rango[0] <= v <= rango[1]: return v
        except ValueError: pass
        print(f"Ingresa un valor entre {rango[0]} y {rango[1]}.")

# ── Procesamiento ─────────────────────────────────────────────────────────────
def procesar(fav, dificil, horas, promedio):
    misma, pocas, bajo, alto = fav == dificil, horas < 2, promedio < 6.0, promedio >= 9.0
    stats = {
        "h_semana":    horas * 7,
        "h_mes":       round(horas * 7 * 4.3, 1),
        "rendimiento": round(promedio / 10 * 100, 2),
        "indice":      round(math.sqrt(max(promedio, 0.01)) * horas, 4),
        "diferencia":  round(10.0 - promedio, 2),
    }
    perfil = {
        "misma": misma, "pocas": pocas, "bajo": bajo, "alto": alto,
        "contradiccion": misma and alto,
        "refuerzo":      misma or pocas or bajo,
    }
    return stats, perfil

def calcular_riesgo(perfil):
    pesos = {"misma": 30, "pocas": 25, "bajo": 35, "contradiccion": 10}
    p = min(sum(v for k, v in pesos.items() if perfil.get(k)), 100)
    nivel = "Sin riesgo" if p == 0 else "Riesgo bajo" if p <= 30 else "Riesgo medio" if p <= 60 else "Riesgo alto"
    return p, nivel

def compatibilidad_ideal(horas, promedio):
    dist   = math.sqrt(((horas/24)-(3/24))**2 + ((promedio/10)-0.9)**2)
    compat = round(max(0.0, min(100.0, (1 - dist/math.sqrt(2)) * 100)), 2)
    desc   = "Excelente" if compat >= 85 else "Buena" if compat >= 65 else "Moderada" if compat >= 45 else "Baja"
    return compat, desc

def clasificar_habito(horas, promedio):
    total = round((horas/24)*50 + (promedio/10)*50, 2)
    if total >= 75: return total, "Habito Excelente",  "Manten el ritmo y explora temas avanzados."
    if total >= 55: return total, "Habito Regular",    "Incrementa tus horas de repaso diario."
    if total >= 35: return total, "Habito Deficiente", "Establece un horario fijo de estudio."
    return          total,        "Habito Critico",    "Busca apoyo de un tutor o maestro."

def recomendar(fav, perfil):
    if perfil["misma"] and perfil["bajo"]: return "Nivelacion Academica General"
    alertas = [a for c, a in [
        (perfil["contradiccion"], "revisa autopercepcion"),
        (perfil["pocas"],         "mejora habitos"),
        (perfil["bajo"],          "refuerzo necesario"),
    ] if c]
    base = AREAS.get(fav, "Area General")
    if alertas:                               return base + " | " + ", ".join(alertas)
    if perfil["alto"] and not perfil["refuerzo"]: return base + " (Nivel Avanzado)"
    return base

def consejo_ia(fav, nivel, compat, area):
    prompt = (
        f"Soy estudiante de preparatoria. Mi materia favorita es {fav}, "
        f"nivel de riesgo: {nivel}, compatibilidad ideal: {compat}%, "
        f"area recomendada: {area}. "
        f"Dame un consejo academico breve en espanol, maximo 2 oraciones."
    )
    try:
        cuerpo = json.dumps({
            "model": "claude-haiku-4-5-20251001", "max_tokens": 120,
            "messages": [{"role": "user", "content": prompt}]
        }).encode("utf-8")
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages", data=cuerpo,
            headers={"Content-Type": "application/json",
                     "x-api-key": "TU_API_KEY_AQUI", "anthropic-version": "2023-06-01"}
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())["content"][0]["text"].strip()
    except Exception:
        return "Consejo IA no disponible (sin conexion o clave invalida)."

# ── Gráfico comparativo ───────────────────────────────────────────────────────
def barra_panel(valor, maximo, ancho=BAR_W):
    pct = min(valor / maximo, 1.0) if maximo > 0 else 0.0
    r   = round(pct * ancho)
    return BLOQUE * r + VACIO * (ancho - r), round(pct * 100)

def linea_panel(contenido, ancho=PANEL_W):
    return f"| {contenido:<{ancho}} |"

def animar_paneles(panel_izq, panel_der, pasos=20):
    ancho   = PANEL_W
    sep_top = "+" + "=" * (ancho + 2) + "+"
    sep_mid = "+" + "-" * (ancho + 2) + "+"

    def construir(indicadores, factor):
        lineas = []
        for nombre, valor, maximo in indicadores:
            barra, pct = barra_panel(valor * factor, maximo, ancho - 2)
            lineas += [
                linea_panel(f"{nombre:<10} {pct:>3}%", ancho),
                linea_panel(f"[{barra}]", ancho),
                linea_panel(f"{round(valor*factor,1)}/{round(maximo,1)}".center(ancho), ancho),
                sep_mid,
            ]
        return lineas

    total = len(construir(panel_izq, 1.0))
    for paso in range(pasos + 1):
        f = paso / pasos
        li, ld = construir(panel_izq, f), construir(panel_der, f)
        if paso > 0:
            try: print(f"\033[{total}A", end="")
            except: pass
        for a, b in zip(li, ld): print(f"  {a}   {b}")
        time.sleep(0.05)

def mostrar_grafico(fav, dificil, horas, promedio, stats, perfil,
                    riesgo, nivel, compat, desc, hab_total, hab_cat, hab_rec):
    limpiar()
    W   = 62
    sep = "=" * W
    nom_fav, nom_dif = NOMBRES.get(fav, fav.title()), NOMBRES.get(dificil, dificil.title())

    print(f"\n  {sep}")
    print(f"  {'ORIENTADOR ACADEMICO  -  PERFIL COMPARATIVO'.center(W)}")
    print(f"  {datetime.datetime.now().strftime('%d/%m/%Y  %H:%M').center(W)}")
    print(f"  {sep}\n"); time.sleep(0.3)

    # Cabeceras de panel
    ancho   = PANEL_W
    sep_top = "+" + "=" * (ancho + 2) + "+"
    sep_mid = "+" + "-" * (ancho + 2) + "+"
    for cab_izq, cab_der in zip(
        [sep_top, linea_panel(nom_fav[:ancho].center(ancho)),
         linea_panel("*** FAVORITA ***".center(ancho)), sep_mid],
        [sep_top, linea_panel(nom_dif[:ancho].center(ancho)),
         linea_panel("*** DIFICIL ***".center(ancho)),  sep_mid],
    ):
        escribir_lento(f"  {cab_izq}   {cab_der}", delay=0.008)
    time.sleep(0.2)

    animar_paneles(
        [("Horas/dia", float(horas), 24.0), ("Promedio", promedio, 10.0), ("Rendimiento", stats["rendimiento"], 100.0)],
        [("Riesgo",    float(riesgo), 100.0), ("Compat.", compat, 100.0), ("Habito", hab_total, 100.0)],
    ); time.sleep(0.3)

    # Areas
    print(f"\n  {sep}")
    escribir_lento(f"  AREA (FAVORITA) : {AREAS.get(fav,'Area General')}", delay=0.018)
    escribir_lento(f"  AREA (DIFICIL)  : {AREAS.get(dificil,'Area General')}", delay=0.018)
    print(f"  {sep}")

    # Comparacion directa
    print(); escribir_lento("  COMPARACION DIRECTA:", delay=0.02)
    print(f"  {'-'*W}")
    for nombre, valor, maximo, desc_txt in [
        ("Promedio", promedio,        10.0,  "Rendimiento academico general"),
        ("Riesgo",   float(riesgo),  100.0,  "Nivel de riesgo detectado"),
        ("Compat.",  compat,         100.0,  "Ajuste al perfil ideal"),
        ("Habito",   hab_total,      100.0,  "Calidad del habito de estudio"),
    ]:
        barra, pct = barra_panel(valor, maximo, ancho=36)
        escribir_lento(f"  {nombre:<10} [{barra}] {pct:>3}%  {desc_txt}", delay=0.007)
        time.sleep(0.08)
    print(f"  {'-'*W}")

    # Alertas
    print(); escribir_lento("  ALERTAS DEL PERFIL:", delay=0.02)
    for nombre, activa in [
        ("Fav == Dificil", perfil["misma"]), ("Pocas horas",    perfil["pocas"]),
        ("Promedio bajo",  perfil["bajo"]),  ("Contradiccion",  perfil["contradiccion"]),
    ]:
        escribir_lento(f"    {'[!!!]' if activa else '[ ok]'}  {nombre}", delay=0.014)
        time.sleep(0.04)

    # Resumen
    print(f"\n  {sep}")
    for linea in [
        f"RIESGO     : {riesgo}/100   ->  {nivel}",
        f"COMPAT.    : {compat}%     ->  {desc}",
        f"HABITO     : {hab_total}/100   ->  {hab_cat}",
        f"ACCION     : {hab_rec}",
    ]: escribir_lento(f"  {linea}", delay=0.018)
    print(f"  {sep}\n")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    limpiar()
    if any(m not in AREAS or m not in NOMBRES for m in MATERIAS):
        print("Error de configuracion."); return

    print("=" * 54 + "\n         ORIENTADOR ACADEMICO\n" + "=" * 54)
    try:
        print("Materias disponibles:")
        for m in MATERIAS: print(f"  - {m}")

        fav      = pedir_materia("Materia favorita    : ")
        dificil  = pedir_materia("Materia dificil     : ")
        horas    = pedir_dato("Horas de estudio (1-24)    : ", int,   (1, 24))
        promedio = pedir_dato("Promedio general (0.0-10.0): ", float, (0.0, 10.0))

        if promedio == 0.0:
            print("Aviso: promedio 0.0, el indice de desempeno sera 0.")

        animacion("Procesando", 2)

        stats, perfil               = procesar(fav, dificil, horas, promedio)
        riesgo, nivel               = calcular_riesgo(perfil)
        compat, desc                = compatibilidad_ideal(horas, promedio)
        hab_total, hab_cat, hab_rec = clasificar_habito(horas, promedio)
        area                        = recomendar(fav, perfil)
        ia                          = consejo_ia(NOMBRES.get(fav, fav), nivel, compat, area)

        sep = "-" * 54
        print(f"\n{sep}")
        print(f"  Fav / Dificil : {NOMBRES.get(fav, fav.title())} / {NOMBRES.get(dificil, dificil.title())}")
        print(f"  Horas         : {horas}/dia | Semana: {stats['h_semana']} | Mes: {stats['h_mes']}")
        print(f"  Promedio      : {promedio} ({stats['rendimiento']}%) | Indice: {stats['indice']}")
        print(f"  AREA          : {area}")
        print(f"  Consejo local : {random.choice(CONSEJOS)}")
        print(sep)
        print(f"  [F.NUEVA 1] Riesgo  : {riesgo}/100 -> {nivel}")
        print(f"  [F.NUEVA 2] Compat. : {compat}%   -> {desc}")
        print(f"  [F.NUEVA 3] Habito  : {hab_total}/100 -> {hab_cat}")
        print(f"              Accion  : {hab_rec}")
        print(sep)
        print(f"  [IAGEN - Claude] {ia}")
        print(sep)

        mostrar_grafico(fav, dificil, horas, promedio, stats, perfil,
                        riesgo, nivel, compat, desc, hab_total, hab_cat, hab_rec)

    except KeyboardInterrupt: print("\nInterrumpido.")
    except Exception as e:    print(f"Error ({type(e).__name__}): {e}")

main()
