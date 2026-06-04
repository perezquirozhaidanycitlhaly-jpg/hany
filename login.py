import tkinter as tk
from tkinter import messagebox

# =========================
# COLORES (FONDO CLARO)
# =========================
BG = "#f5f7ff"
ACCENT = "#4a6fff"
ACCENT2 = "#ff4fd8"
TEXT = "#1a1a1a"
BTN = "#ffd60a"
RED = "#ff0000"

# =========================
# LOGIN SIMULADO
# =========================
USUARIO_VALIDO = "alumno"
PASSWORD_VALIDA = "1234"

root = tk.Tk()
root.title("🎮 School Game Login")
root.geometry("900x600")
root.config(bg=BG)

# =========================
# FUNCIONES
# =========================
def entrar():
    u = entry_user.get()
    p = entry_pass.get()

    if u == USUARIO_VALIDO and p == PASSWORD_VALIDA:
        messagebox.showinfo("Bienvenido", "¡Entraste al juego!")
        login_frame.pack_forget()
        game_frame.pack(fill="both", expand=True)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def guardar():
    fav = entry_fav.get()
    diff = entry_diff.get()
    horas = entry_hours.get()

    try:
        horas = int(horas)
    except:
        messagebox.showerror("Error", "Las horas deben ser número")
        return

    # =========================
    # MENSAJES SEGÚN HORAS
    # =========================
    if horas >= 5:
        msg = "🔥 ¡Excelente! Tus horas de estudio son muy buenas"
    elif horas >= 3:
        msg = "📘 Vas bien, pero puedes mejorar un poco"
    else:
        msg = "⚠️ Estás estudiando poco\n💪 No te rindas, tú puedes mejorar con esfuerzo"

    resultado.config(text=f"""
🎮 PERFIL DEL JUGADOR

📚 Materia favorita: {fav}
⚠️ Materia difícil: {diff}
⏰ Horas de estudio: {horas}

{msg}

✨ LO MEJOR DE LA PREPA ES CUANDO SALIMOS DE VACACIONES

🔴 YA SUELTENOS PROFE FERNANDO
""", fg=TEXT)

# =========================
# LOGIN UI
# =========================
login_frame = tk.Frame(root, bg=BG)
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="🎮 SCHOOL GAME LOGIN",
         fg=ACCENT, bg=BG, font=("Arial", 24, "bold")).pack(pady=40)

tk.Label(login_frame, text="Usuario", fg=TEXT, bg=BG).pack()
entry_user = tk.Entry(login_frame, font=("Arial", 14))
entry_user.pack(pady=5)

tk.Label(login_frame, text="Contraseña", fg=TEXT, bg=BG).pack()
entry_pass = tk.Entry(login_frame, font=("Arial", 14), show="*")
entry_pass.pack(pady=5)

tk.Button(login_frame, text="Entrar ▶", bg=BTN,
          font=("Arial", 14, "bold"), command=entrar).pack(pady=20)

# =========================
# JUEGO UI
# =========================
game_frame = tk.Frame(root, bg=BG)

tk.Label(game_frame, text="🎯 TU PERFIL DE ESTUDIANTE",
         fg=ACCENT2, bg=BG, font=("Arial", 22, "bold")).pack(pady=10)

tk.Label(game_frame, text="Materia favorita", fg=TEXT, bg=BG).pack()
entry_fav = tk.Entry(game_frame, font=("Arial", 14))
entry_fav.pack(pady=5)

tk.Label(game_frame, text="Materia difícil", fg=TEXT, bg=BG).pack()
entry_diff = tk.Entry(game_frame, font=("Arial", 14))
entry_diff.pack(pady=5)

tk.Label(game_frame, text="Horas de estudio", fg=TEXT, bg=BG).pack()
entry_hours = tk.Entry(game_frame, font=("Arial", 14))
entry_hours.pack(pady=5)

tk.Button(game_frame, text="Guardar progreso 💾",
          bg=ACCENT, font=("Arial", 14, "bold"),
          command=guardar).pack(pady=15)

resultado = tk.Label(game_frame, text="", fg=TEXT,
                     bg=BG, font=("Arial", 14), justify="left")
resultado.pack(pady=20)

root.mainloop()