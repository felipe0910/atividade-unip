import tkinter as tk
from tkinter import messagebox
import json
import os
from cadastro_professor import tela_cadastro
from sistema import painel_professor
# OU, se a função estiver em login_prof.py ou outro arquivo:
# from seu_modulo_correto import painel_professor



ARQUIVO_PROFESSORES = "professores.json"

COR_FUNDO = "#f2f2f2"
COR_FRAME = "#ecf0f1"
COR_TITULO = "#2c3e50"
COR_BOTAO = "#2980b9"
COR_TEXTO_BOTAO = "white"

def carregar_professores():
    if os.path.exists(ARQUIVO_PROFESSORES):
        with open(ARQUIVO_PROFESSORES, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def tela_login():
    def validar_login():
        email = entry_email.get().strip()
        senha = entry_senha.get().strip()

        professores = carregar_professores()

        for p in professores:
            if p["email"] == email and p["senha"] == senha:
                messagebox.showinfo("Login", "✅ Login realizado com sucesso!")
                janela_login.destroy()
                painel_professor()
                return

        messagebox.showerror("Erro", "❌ E-mail ou senha incorretos!")

    janela_login = tk.Tk()
    janela_login.title("Login do Professor")
    janela_login.geometry("400x300")
    janela_login.config(bg=COR_FUNDO)

    frame_login = tk.Frame(janela_login, bg=COR_FRAME, padx=20, pady=20, relief="groove", bd=2)
    frame_login.pack(pady=30)

    tk.Label(frame_login, text="Acesso do Professor", font=("Arial", 14, "bold"), bg=COR_FRAME, fg=COR_TITULO).pack(pady=10)
    tk.Label(frame_login, text="E-mail:", bg=COR_FRAME).pack(anchor="w")
    entry_email = tk.Entry(frame_login, width=30)
    entry_email.pack(pady=5)

    tk.Label(frame_login, text="Senha:", bg=COR_FRAME).pack(anchor="w")
    entry_senha = tk.Entry(frame_login, show="*", width=30)
    entry_senha.pack(pady=5)

    tk.Button(frame_login, text="Entrar", command=validar_login, bg=COR_BOTAO, fg=COR_TEXTO_BOTAO, width=20).pack(pady=10)
    tk.Button(frame_login, text="Cadastrar Professor", command=tela_cadastro, bg="#27ae60", fg="white", width=20).pack(pady=5)

    janela_login.mainloop()

if __name__ == "__main__":
    tela_login()
