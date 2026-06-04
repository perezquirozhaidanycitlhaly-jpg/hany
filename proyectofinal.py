# =========================================================
# SISTEMA ESCOLAR COMPLETO
# TODO EN UN SOLO CODIGO
# =========================================================

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