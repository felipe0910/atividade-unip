import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO_PROFESSORES = "professores.json"

def carregar_professores():
    if os.path.exists(ARQUIVO_PROFESSORES):
        with open(ARQUIVO_PROFESSORES, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_professores(lista):
    with open(ARQUIVO_PROFESSORES, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

def tela_cadastro():
    def cadastrar():
        email = entry_email.get().strip()
        senha = entry_senha.get().strip()

        if not email or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        professores = carregar_professores()
        if any(p["email"] == email for p in professores):
            messagebox.showerror("Erro", "E-mail já cadastrado!")
            return

        professores.append({"email": email, "senha": senha})
        salvar_professores(professores)
        messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")
        janela_cadastro.destroy()

    janela_cadastro = tk.Tk()  # <-- Pode usar Tk se quiser rodar sozinho
    janela_cadastro.title("Cadastro de Professor")
    janela_cadastro.geometry("400x250")
    janela_cadastro.config(bg="#f2f2f2")

    frame = tk.Frame(janela_cadastro, bg="#ecf0f1", padx=20, pady=20, relief="groove", bd=2)
    frame.pack(pady=30)

    tk.Label(frame, text="Cadastro de Professor", font=("Arial", 14, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=10)
    tk.Label(frame, text="E-mail:", bg="#ecf0f1").pack(anchor="w")
    entry_email = tk.Entry(frame, width=30)
    entry_email.pack(pady=5)

    tk.Label(frame, text="Senha:", bg="#ecf0f1").pack(anchor="w")
    entry_senha = tk.Entry(frame, show="*", width=30)
    entry_senha.pack(pady=5)

    tk.Button(frame, text="Cadastrar", command=cadastrar, bg="#2980b9", fg="white", width=20).pack(pady=15)


if __name__ == "__main__":
    tela_cadastro()
    tk.mainloop()
