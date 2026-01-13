import tkinter as tk
from tkinter import messagebox, simpledialog
import alunos
import subprocess
import os
import sys

# --- Configurações de Cores e Ícones ---
COR_FUNDO = "#f2f2f2"
COR_TITULO = "#2c3e50"
COR_BOTAO = "#2980b9"
COR_TEXTO_BOTAO = "white"
COR_FRAME = "#ecf0f1"

ICONE_INSERIR = "➕"
ICONE_LISTAR = "📋"
ICONE_NOTAS = "📝"
ICONE_ATUALIZAR = "🔄"
ICONE_DELETAR = "🗑️"

def painel_professor():
    janela = tk.Tk()
    janela.title("Painel do Professor")
    janela.geometry("600x450")
    janela.config(bg=COR_FUNDO)

    header_frame = tk.Frame(janela, bg=COR_BOTAO, pady=10)
    header_frame.pack(fill="x")
    tk.Label(header_frame, text="Painel do Professor", font=("Arial", 16, "bold"), bg=COR_BOTAO, fg="white").pack()

    content_frame = tk.Frame(janela, bg=COR_FUNDO, pady=10)
    content_frame.pack(expand=True, fill="both")

    botoes_frame = tk.LabelFrame(content_frame, text="Gerenciar Alunos", bg=COR_FRAME, padx=20, pady=20,
                                 font=("Arial", 11, "bold"), fg=COR_TITULO)
    botoes_frame.pack(padx=20, pady=20, fill="both", expand=True)

    def listar_alunos():
        lista = alunos.carregar_alunos()
        texto = "RA | Nome | NP1 | NP2 | PIM | Média | Situação\n"
        texto += "-" * 60 + "\n"

        for a in lista:
            np1 = a.get("NP1", "N/A")
            np2 = a.get("NP2", "N/A")
            pim = a.get("PIM", "N/A")
            media = a.get("Media", "N/A")
            situacao = a.get("Situacao", "N/A")

            np1_str = f"{np1:.1f}" if isinstance(np1, (float, int)) else str(np1)
            np2_str = f"{np2:.1f}" if isinstance(np2, (float, int)) else str(np2)
            pim_str = f"{pim:.1f}" if isinstance(pim, (float, int)) else str(pim)
            media_str = f"{media:.2f}" if isinstance(media, (float, int)) else str(media)

            texto += f"{a['RA']} | {a['nome']} | {np1_str} | {np2_str} | {pim_str} | {media_str} | {situacao}\n"

        messagebox.showinfo("Lista de Alunos", texto if lista else "Nenhum aluno cadastrado.")

    def inserir_aluno():
        ra = simpledialog.askstring("Novo Aluno", "Digite o RA:")
        nome = simpledialog.askstring("Novo Aluno", "Digite o nome do aluno:")
        if ra and nome:
            alunos_lista = alunos.carregar_alunos()
            if any(a["RA"] == ra for a in alunos_lista):
                messagebox.showerror("Erro", "RA já cadastrado!")
                return
            
            novo = {"RA": ra, "nome": nome, "NP1": None, "NP2": None, "PIM": None, "Media": None, "Situacao": None}
            alunos_lista.append(novo)
            alunos.salvar_alunos(alunos_lista)
            messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado!")

    def inserir_notas():
        ra = simpledialog.askstring("Inserir Notas", "Digite o RA do aluno:")
        if not ra:
            return
        
        alunos_lista = alunos.carregar_alunos()
        for a in alunos_lista:
            if a["RA"] == ra:
                try:
                    np1_str = simpledialog.askstring("Notas", "Digite a nota da NP1:")
                    np2_str = simpledialog.askstring("Notas", "Digite a nota da NP2:")
                    pim_str = simpledialog.askstring("Notas", "Digite a nota do PIM:")

                    if np1_str is None or np2_str is None or pim_str is None:
                        return

                    if not np1_str.strip() or not np2_str.strip() or not pim_str.strip():
                        messagebox.showerror("Erro", "Todas as notas são obrigatórias.")
                        return

                    np1 = float(np1_str.replace(",", "."))
                    np2 = float(np2_str.replace(",", "."))
                    pim = float(pim_str.replace(",", "."))

                    a["NP1"], a["NP2"], a["PIM"] = np1, np2, pim

                    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
                    exe_path = os.path.join(script_dir, "calculo_media.exe")

                    processo = subprocess.run(
                        [exe_path],
                        input=f"{np1} {np2} {pim}",
                        text=True,
                        capture_output=True,
                        check=True
                    )

                    saida = processo.stdout.strip()
                    import re
                    match = re.search(r"([0-9]+(?:\.[0-9]+)?)", saida)
                    if not match:
                        raise ValueError("Saída inválida do cálculo")

                    media = float(match.group(1))
                    saida_up = saida.upper()

                    if "APROV" in saida_up:
                        situacao = "Aprovado"
                    elif "RECU" in saida_up:
                        situacao = "Recuperacao"
                    else:
                        situacao = "Reprovado"

                    a["Media"] = media
                    a["Situacao"] = situacao
                    alunos.salvar_alunos(alunos_lista)

                    messagebox.showinfo("Resultado",
                        f"✅ Notas salvas!\n📊 Média: {media:.2f}\n⭐ Situação: {situacao}"
                    )
                    return

                except ValueError:
                    messagebox.showerror("Erro", "Digite apenas números.")
                    return
                except FileNotFoundError:
                    messagebox.showerror("Erro", "calculo_media.exe não encontrado!")
                    return

        messagebox.showerror("Erro", "RA não encontrado!")

    def atualizar_aluno():
        ra = simpledialog.askstring("Atualizar", "Digite o RA:")
        if not ra: return

        alunos_lista = alunos.carregar_alunos()
        for a in alunos_lista:
            if a["RA"] == ra:
                nome = simpledialog.askstring("Atualizar", "Novo nome:")
                if nome:
                    a["nome"] = nome
                    alunos.salvar_alunos(alunos_lista)
                    messagebox.showinfo("Sucesso", "Nome atualizado!")
                return
        
        messagebox.showerror("Erro", "RA não encontrado!")

    def deletar_aluno():
        ra = simpledialog.askstring("Deletar", "RA do aluno:")
        if not ra: return
        
        alunos_lista = alunos.carregar_alunos()
        nova_lista = [a for a in alunos_lista if a["RA"] != ra]

        if len(nova_lista) < len(alunos_lista):
            alunos.salvar_alunos(nova_lista)
            messagebox.showinfo("Sucesso", "Aluno removido!")
        else:
            messagebox.showerror("Erro", "RA não encontrado!")

    estilo = {'bg': COR_BOTAO, 'fg': COR_TEXTO_BOTAO, 'font': ('Arial', 10, 'bold'), 'width': 25, 'pady': 5, 'compound': 'left'}

    tk.Button(botoes_frame, text=ICONE_INSERIR + " Inserir Aluno", command=inserir_aluno, **estilo).pack(pady=5)
    tk.Button(botoes_frame, text=ICONE_LISTAR + " Listar Alunos", command=listar_alunos, **estilo).pack(pady=5)
    tk.Button(botoes_frame, text=ICONE_NOTAS + " Inserir Notas", command=inserir_notas, **estilo).pack(pady=5)
    tk.Button(botoes_frame, text=ICONE_ATUALIZAR + " Atualizar Nome", command=atualizar_aluno, **estilo).pack(pady=5)
    tk.Button(botoes_frame, text=ICONE_DELETAR + " Excluir Aluno", command=deletar_aluno, **estilo).pack(pady=5)

    janela.mainloop()

def iniciar_painel_professor():
    painel_professor()
