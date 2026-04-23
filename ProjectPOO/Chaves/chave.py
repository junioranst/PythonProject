import json
import os
from tkinter import messagebox
from customtkinter import *

# Configurações globais de aparência
set_appearance_mode("dark")
set_default_color_theme("blue")


class Chave:
    def __init__(self, nome, cidade, quantidade, emprestadas=0, possuidores=None):
        self.nome = nome
        self.cidade = cidade
        self.quantidade = int(quantidade)
        self.emprestadas = int(emprestadas)
        self.possuidores = possuidores if possuidores else []


class ControleChaves:
    def __init__(self):
        self.chaves = []
        self.arquivo_dados = "controle_chaves.json"
        self.carregar_dados()

        self.root = CTk()
        self.root.title("Controle de Chaves Pro - Adriano")
        self.root.geometry("1200x700")

        # --- Menu Lateral ---
        self.frame_menu = CTkFrame(self.root, width=240, corner_radius=0)
        self.frame_menu.pack(side=LEFT, fill=Y)

        CTkLabel(self.frame_menu, text="SISTEMA CHAVES", font=("Arial", 22, "bold"), text_color="white").pack(pady=40)

        btn_style = {"width": 210, "height": 45, "font": ("Arial", 13, "bold")}

        CTkButton(self.frame_menu, text="➕ Cadastrar Chave", command=self.janela_cadastrar, **btn_style).pack(pady=10)
        CTkButton(self.frame_menu, text="📋 Listar Todas", command=self.atualizar_lista, **btn_style).pack(pady=10)
        CTkButton(self.frame_menu, text="⚠️ Exibir Emprestadas", command=self.listar_emprestadas, fg_color="#e67e22",
                  hover_color="#d35400", **btn_style).pack(pady=10)
        CTkButton(self.frame_menu, text="🔍 Buscar Chave", command=self.buscar_chave, **btn_style).pack(pady=10)
        CTkButton(self.frame_menu, text="📤 Emprestar", command=self.registrar_emprestimo, **btn_style).pack(pady=10)
        CTkButton(self.frame_menu, text="📥 Devolver", command=self.registrar_devolucao, **btn_style).pack(pady=10)

        CTkButton(self.frame_menu, text="❌ Sair", command=self.root.quit, fg_color="#c0392b", hover_color="#962d22",
                  **btn_style).pack(side=BOTTOM, pady=30)

        # --- Área Principal ---
        self.area_principal = CTkScrollableFrame(self.root, label_text="Painel de Inventário")
        self.area_principal.pack(side=RIGHT, expand=True, fill=BOTH, padx=20, pady=20)

        self.atualizar_lista()
        self.root.mainloop()

    # --- Persistência de Dados ---
    def salvar_dados(self):
        dados = [vars(c) for c in self.chaves]
        with open(self.arquivo_dados, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar_dados(self):
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, "r", encoding="utf-8") as f:
                    self.chaves = [Chave(**d) for d in json.load(f)]
            except:
                self.chaves = []

    # --- Interface de Listagem ---
    def atualizar_lista(self, lista_custom=None):
        for widget in self.area_principal.winfo_children(): widget.destroy()
        exibir = lista_custom if lista_custom is not None else self.chaves

        for c in exibir:
            card = CTkFrame(self.area_principal, height=90)
            card.pack(fill=X, pady=8, padx=10)

            disponiveis = c.quantidade - c.emprestadas
            if c.emprestadas == 0:
                status_txt, status_cor = "DISPONÍVEL", "#2ecc71"
            elif disponiveis > 0:
                status_txt, status_cor = "EMPRESTADA", "#f1c40f"
            else:
                status_txt, status_cor = "INDISPONÍVEL", "#e74c3c"

            # --- LADO ESQUERDO: INFOS ---
            frame_info = CTkFrame(card, fg_color="transparent")
            frame_info.pack(side=LEFT, padx=20, pady=10)

            CTkLabel(frame_info, text=f"{c.nome.upper()} ({c.cidade})", text_color="white",
                     font=("Arial", 16, "bold")).pack(anchor="w")

            # Sub-frame para as quantidades com cores mistas
            frame_qnt = CTkFrame(frame_info, fg_color="transparent")
            frame_qnt.pack(anchor="w")

            f_lbl, f_num = ("Arial", 14, "bold"), ("Arial", 15, "bold")
            c_azul, c_branco = "#3498db", "#FFFFFF"

            CTkLabel(frame_qnt, text="Total: ", text_color=c_azul, font=f_lbl).pack(side=LEFT)
            CTkLabel(frame_qnt, text=f"{c.quantidade}", text_color=c_branco, font=f_num).pack(side=LEFT)
            CTkLabel(frame_qnt, text="  |  ", text_color=c_azul, font=f_lbl).pack(side=LEFT)
            CTkLabel(frame_qnt, text="No Estoque: ", text_color=c_azul, font=f_lbl).pack(side=LEFT)
            CTkLabel(frame_qnt, text=f"{disponiveis}", text_color=c_branco, font=f_num).pack(side=LEFT)

            # --- LADO DIREITO: STATUS E AÇÕES ---
            frame_acoes = CTkFrame(card, fg_color="transparent")
            frame_acoes.pack(side=RIGHT, padx=20)

            CTkButton(frame_acoes, text="X", width=35, height=35, fg_color="#c0392b", hover_color="#962d22",
                      command=lambda obj=c: self.excluir_chave(obj)).pack(side=RIGHT, padx=(15, 0))

            posse_txt = f"({', '.join(c.possuidores)})" if c.possuidores else "(Inventário)"
            CTkLabel(frame_acoes, text=status_txt, text_color=status_cor, font=("Arial", 15, "bold")).pack(side=RIGHT,
                                                                                                           padx=5)
            CTkLabel(frame_acoes, text=posse_txt, text_color="gray", font=("Arial", 12)).pack(side=RIGHT, padx=5)

    def excluir_chave(self, chave_obj):
        if messagebox.askyesno("Confirmar Exclusão", f"Deseja remover a chave '{chave_obj.nome}'?"):
            self.chaves.remove(chave_obj)
            self.salvar_dados()
            self.atualizar_lista()

    def listar_emprestadas(self):
        emprestadas = [c for c in self.chaves if c.emprestadas > 0]
        self.atualizar_lista(emprestadas)

    def registrar_emprestimo(self):
        diag = CTkInputDialog(text="Nome da chave para retirar:", title="Empréstimo")
        nome = diag.get_input()
        if not nome: return

        for c in self.chaves:
            if c.nome.lower() == nome.lower():
                if c.emprestadas < c.quantidade:
                    pessoa = CTkInputDialog(text="Nome de quem está retirando:", title="Identificação").get_input()
                    if pessoa:
                        c.emprestadas += 1
                        c.possuidores.append(pessoa)
                        self.salvar_dados()
                        self.atualizar_lista()
                        messagebox.showinfo("Sucesso", f"Chave retirada por: {pessoa}")
                    return
                else:
                    messagebox.showwarning("Esgotado", "Não há mais cópias disponíveis!")
                return
        messagebox.showerror("Erro", "Chave não encontrada.")

    def registrar_devolucao(self):
        diag = CTkInputDialog(text="Qual chave será devolvida?", title="Devolução")
        nome = diag.get_input()
        if not nome: return

        for c in self.chaves:
            if c.nome.lower() == nome.lower() and c.emprestadas > 0:
                if c.possuidores:
                    pessoa_removida = c.possuidores.pop()
                    c.emprestadas -= 1
                    self.salvar_dados()
                    self.atualizar_lista()
                    messagebox.showinfo("Sucesso", f"Devolução registrada: {pessoa_removida}")
                    return
        messagebox.showerror("Erro", "Chave não encontrada ou estoque já está cheio.")

    def janela_cadastrar(self):
        janela = CTkToplevel()
        janela.title("Cadastrar Nova Chave")
        janela.geometry("350x420")
        janela.attributes("-topmost", True)

        CTkLabel(janela, text="Nome da Chave:", font=("Arial", 13)).pack(pady=(20, 5))
        en = CTkEntry(janela, width=250);
        en.pack()
        CTkLabel(janela, text="Cidade / Unidade:", font=("Arial", 13)).pack(pady=10)
        ec = CTkEntry(janela, width=250);
        ec.pack()
        CTkLabel(janela, text="Quantidade de Cópias:", font=("Arial", 13)).pack(pady=10)
        eq = CTkEntry(janela, width=250);
        eq.pack()

        def confirm():
            if en.get() and ec.get() and eq.get().isdigit():
                self.chaves.append(Chave(en.get(), ec.get(), eq.get()))
                self.salvar_dados()
                self.atualizar_lista()
                janela.destroy()
            else:
                messagebox.showwarning("Erro", "Preencha os campos corretamente.")

        CTkButton(janela, text="SALVAR NO INVENTÁRIO", command=confirm, width=250, height=45,
                  font=("Arial", 13, "bold")).pack(pady=35)

    def buscar_chave(self):
        termo = CTkInputDialog(text="Busque por nome ou cidade:", title="Busca").get_input()
        if termo:
            res = [c for c in self.chaves if termo.lower() in c.nome.lower() or termo.lower() in c.cidade.lower()]
            self.atualizar_lista(res)


if __name__ == "__main__":
    ControleChaves()