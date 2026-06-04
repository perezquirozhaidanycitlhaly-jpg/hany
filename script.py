# ==========================================
# LOGO ESCOLAR FUTURISTA AJUSTADO
# Ahora se ve completo en la ventana
# ==========================================

import tkinter as tk, random, math

# Ventana más pequeña
w,h=1100,700

r=tk.Tk()
r.title("Logo Escolar")
r.geometry(f"{w}x{h}")
r.config(bg="#040814")

c=tk.Canvas(r,width=w,height=h,bg="#040814",highlightthickness=0)
c.pack()

# Fondo digital
for i in range(0,w,40):
    c.create_line(i,0,i,h,fill="#091220")

for i in range(0,h,40):
    c.create_line(0,i,w,i,fill="#091220")

# Partículas
p=[]

for _ in range(60):
    x,y=random.randint(0,w),random.randint(0,h)

    o=c.create_oval(
        x,y,x+3,y+3,
        fill=random.choice([
            "#00ffff",
            "#00ff99",
            "#ffffff",
            "#ff00ff"
        ]),
        outline=""
    )

    p.append([o,x,y])

# Aros
c.create_oval(
    180,20,920,680,
    outline="#00ffff",
    width=4
)

c.create_oval(
    210,50,890,650,
    outline="#ff00ff",
    width=2
)

# Rayos
for _ in range(8):
    c.create_text(
        random.randint(200,900),
        random.randint(50,650),
        text="⚡",
        fill=random.choice([
            "#ffd700",
            "#00ffff",
            "#ff00ff"
        ]),
        font=("Arial",18)
    )

# Glow búho
c.create_oval(
    350,100,760,520,
    fill="#170d2b",
    outline=""
)

# Cabeza
c.create_oval(
    390,120,730,460,
    fill="#8B4513",
    outline="#2e1608",
    width=5
)

# Orejas
c.create_polygon(
    450,170,520,50,580,210,
    fill="#5c2f0d",
    outline="black",
    width=3
)

c.create_polygon(
    580,210,650,50,710,170,
    fill="#5c2f0d",
    outline="black",
    width=3
)

# Sombrero
c.create_polygon(
    420,110,560,30,720,110,560,170,
    fill="#101010",
    outline="white",
    width=2
)

# Ojos
for x in [460,560]:
    c.create_oval(
        x,200,x+110,310,
        fill="white",
        outline="black",
        width=4
    )

# Iris
for x in [500,600]:
    c.create_oval(
        x,240,x+35,275,
        fill="#00aaff"
    )

# Pupilas
for x in [512,612]:
    c.create_oval(
        x,252,x+10,262,
        fill="black"
    )

# Pico
c.create_polygon(
    540,320,580,320,560,370,
    fill="#ffb000",
    outline="black",
    width=2
)

# Libro
c.create_rectangle(
    420,390,700,490,
    fill="#003cff",
    outline="white",
    width=4
)

c.create_line(
    560,390,560,490,
    fill="white",
    width=3
)

# Líneas libro
for i in range(5):

    y=410+i*15

    c.create_line(
        440,y,545,y,
        fill="#dce6ff",
        width=2
    )

    c.create_line(
        575,y,680,y,
        fill="#dce6ff",
        width=2
    )

# Texto principal
c.create_text(
    550,560,
    text="ESTUDIO",
    fill="#00aaff",
    font=("Arial Black",42)
)

c.create_text(
    548,556,
    text="ESTUDIO",
    fill="white",
    font=("Arial Black",42)
)

c.create_text(
    550,620,
    text="CON PROPÓSITO",
    fill="#ffd400",
    font=("Arial Black",26)
)

# Laterales
c.create_text(
    120,180,
    text="📚",
    font=("Arial",60)
)

c.create_text(
    120,260,
    text="MATERIA\nFAVORITA",
    fill="#00ff88",
    font=("Arial Black",18)
)

c.create_text(
    980,180,
    text="🧠",
    font=("Arial",60)
)

c.create_text(
    980,260,
    text="MATERIA\nDIFÍCIL",
    fill="#ff4444",
    font=("Arial Black",18)
)

c.create_text(
    120,520,
    text="⏰",
    font=("Arial",60)
)

c.create_text(
    120,610,
    text="HORAS DE\nESTUDIO",
    fill="#00ccff",
    font=("Arial Black",18)
)

# Libros laterales
y=450

for color in [
    "#00cc44",
    "#0044ff",
    "#ff3333",
    "#ffd700"
]:

    c.create_rectangle(
        930,y,1060,y+40,
        fill=color,
        outline="white",
        width=2
    )

    y+=40

# Frase
c.create_text(
    550,680,
    text="El conocimiento es el poder del futuro",
    fill="#cccccc",
    font=("Arial",14,"italic")
)

# Animación
a=0

def anim():

    global a
    a+=0.08

    for o,x,y in p:

        ny=y+math.sin(a+x/50)*0.6

        c.coords(
            o,
            x,ny,
            x+3,ny+3
        )

    r.after(40,anim)

anim()

# ========================================================
# SISTEMA ESCOLAR COMPLETO
# TODO EN UN SOLO CODIGO
# ========================================================

# =========================
# LIBRERIAS
# =========================

import getpass
import base64
import csv
import sqlite3
import os
import time

# =========================
# LOGIN VISUAL
# =========================

print("""
========================================================
                SISTEMA ESCOLAR CBTA 217
========================================================

                      /|     |\\
                     / |     | \\
                    /  |_____|  \\
                   /   ( o o )   \\
                  /_____|^|_______\\
                         |
                      \\_____/


                  BUHO DE SEGURIDAD
========================================================
""")

time.sleep(2)

# =========================
# LOGIN
# =========================

# Usuario correcto
usuario_correcto = "cbta217"

# Contraseña encriptada
password_encriptada = "cnVlbGkzMzM="

# Desencriptar contraseña
password_correcta = base64.b64decode(password_encriptada).decode()

print("===================================")
print("       INICIO DE SESION")
print("===================================")

usuario = input("Usuario: ")

# Contraseña oculta
password = getpass.getpass("Contraseña: ")

# =========================
# VERIFICACION LOGIN
# =========================

if usuario == usuario_correcto and password == password_correcta:

    print("\nAcceso correcto...\n")

    # =========================
    # BIENVENIDA
    # =========================

    print("""
========================================================
            BIENVENIDO AL SISTEMA ESCOLAR
========================================================
""")

    print("""
            /\\_/\\\\
           ( o.o )
            > ^ <
    """)

    # =========================
    # FUNCIONES
    # =========================

    def guardar_csv(nombre, favorita, dificil, horas):

        archivo_existe = os.path.isfile("datos.csv")

        with open("datos.csv", "a", newline="") as archivo:

            escritor = csv.writer(archivo)

            # Encabezados
            if not archivo_existe:
                escritor.writerow([
                    "Nombre",
                    "Materia Favorita",
                    "Materia Dificil",
                    "Horas Estudio"
                ])

            escritor.writerow([
                nombre,
                favorita,
                dificil,
                horas
            ])


    def guardar_db(nombre, favorita, dificil, horas):

        conexion = sqlite3.connect("escuela.db")
        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos(

            nombre TEXT,
            favorita TEXT,
            dificil TEXT,
            horas INTEGER

        )
        """)

        cursor.execute("""
        INSERT INTO alumnos VALUES(?,?,?,?)
        """, (nombre, favorita, dificil, horas))

        conexion.commit()
        conexion.close()


    def procesar_datos(favorita, horas):

        print("\n===================================")
        print("     PROCESAMIENTO DE DATOS")
        print("===================================")

        if horas >= 5:
            print("Excelente dedicación académica")
        else:
            print("Necesitas estudiar más")

        if favorita.lower() == "programacion":
            print("Tienes afinidad con tecnología")
        else:
            print("Interés académico registrado")


    def mostrar_menu():

        print("""
===================================
          MENU PRINCIPAL
===================================

1. Registrar alumno
2. Mostrar mensaje
3. Verificar archivos
4. Salir

===================================
""")


    def verificar_archivos():

        print("\n===================================")
        print("       VERIFICACION FINAL")
        print("===================================")

        if os.path.isfile("datos.csv"):
            print("CSV generado correctamente")
        else:
            print("CSV no encontrado")

        if os.path.isfile("escuela.db"):
            print("Base de datos generada")
        else:
            print("Base de datos no encontrada")

        print("Sistema funcionando correctamente")


    def cierre_sesion():

        print("""
===================================
         CIERRE DE SESION
===================================
""")

        print("Gracias por utilizar el sistema")
        print("Sesion finalizada correctamente")


    # =========================
    # MENU PRINCIPAL
    # =========================

    while True:

        mostrar_menu()

        opcion = input("Selecciona una opción: ")

        # ====================================
        # OPCION 1
        # ====================================

        if opcion == "1":

            print("\n========== FORMULARIO ==========\n")

            nombre = input("Nombre del alumno: ")
            favorita = input("Materia favorita: ")
            dificil = input("Materia más difícil: ")
            horas = int(input("Horas de estudio: "))

            # Guardar archivos
            guardar_csv(nombre, favorita, dificil, horas)
            guardar_db(nombre, favorita, dificil, horas)

            # Procesamiento
            procesar_datos(favorita, horas)

            print("\nDatos guardados correctamente")

        # ====================================
        # OPCION 2
        # ====================================

        elif opcion == "2":

            print("""
===================================
      SISTEMA FUNCIONANDO ✅
===================================
""")

        # ====================================
        # OPCION 3
        # ====================================

        elif opcion == "3":

            verificar_archivos()

        # ====================================
        # OPCION 4
        # ====================================

        elif opcion == "4":

            cierre_sesion()
            break

        # ====================================
        # OPCION INCORRECTA
        # ====================================

        else:

            print("\nOpción incorrecta")

# =========================
# LOGIN INCORRECTO
# =========================

else:

    print("\nERROR ❌")
    print("Usuario o contraseña incorrectos")

r.mainloop()