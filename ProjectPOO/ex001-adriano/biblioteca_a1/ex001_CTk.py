import json
from tkinter import *
from tkinter import messagebox
from customtkinter import *

# Configurações de aparência do CustomTkinter
set_appearance_mode("dark")
set_default_color_theme("blue")


class Livro:
    def __init__(self, titulo, autor, ano, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.carregar_dados()  # Carrega os livros automaticamente ao iniciar

    def salvar_dados(self):
        """Salva a lista de livros em um arquivo JSON"""
        try:
            # Converte os objetos Livro em dicionários para o JSON aceitar
            dados = [vars(l) for l in self.livros]
            with open("biblioteca.json", "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Erro ao Salvar", f"Não foi possível salvar os dados: {e}")

    def carregar_dados(self):
        """Carrega os livros do arquivo JSON se ele existir"""
        try:
            if os.path.exists("biblioteca.json"):
                with open("biblioteca.json", "r", encoding="utf-8") as f:
                    dados_lidos = json.load(f)
                    # Recria os objetos Livro a partir dos dicionários lidos
                    self.livros = [Livro(**d) for d in dados_lidos]
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            self.livros = []

    def adicionar_livros_ui(self, area_texto):
        self.janela_add = CTkToplevel()
        self.janela_add.title("Cadastrar Novo Livro")
        self.janela_add.geometry("350x250")
        self.janela_add.attributes("-topmost", True)

        CTkLabel(self.janela_add, text="Título:").grid(row=0, column=0, padx=20, pady=10)
        ent_titulo = CTkEntry(self.janela_add, width=150)
        ent_titulo.grid(row=0, column=1, padx=20, pady=10)

        CTkLabel(self.janela_add, text="Autor:").grid(row=1, column=0, padx=20, pady=10)
        ent_autor = CTkEntry(self.janela_add, width=150)
        ent_autor.grid(row=1, column=1, padx=20, pady=10)

        CTkLabel(self.janela_add, text="Ano:").grid(row=2, column=0, padx=20, pady=10)
        ent_ano = CTkEntry(self.janela_add, width=150)
        ent_ano.grid(row=2, column=1, padx=20, pady=10)

        def salvar():
            t, aut, ano = ent_titulo.get().strip(), ent_autor.get().strip(), ent_ano.get().strip()
            if t and aut and ano:
                self.livros.append(Livro(t, aut, ano))
                self.salvar_dados()  # SALVA NO ARQUIVO
                self.janela_add.destroy()
                self.listar_livros_ui(area_texto)
                messagebox.showinfo("Sucesso", f"O livro '{t}' foi adicionado!")
            else:
                messagebox.showwarning("Erro", "Preencha todos os campos!")

        CTkButton(self.janela_add, text="Salvar Livro", command=salvar, fg_color="#28a745", hover_color="#218838").grid(
            row=3, columnspan=2, pady=20)

    def formatar_livro(self, area_texto, livro):
        area_texto.insert(END, "Titulo: ", "rotulo")
        area_texto.insert(END, f"{livro.titulo} ", "negrito")
        area_texto.insert(END, "| Autor: ", "rotulo")
        area_texto.insert(END, f"{livro.autor} ", "negrito")
        area_texto.insert(END, "| Ano: ", "rotulo")
        area_texto.insert(END, f"{livro.ano} ", "negrito")
        area_texto.insert(END, "| Status: ", "rotulo")

        if livro.disponivel:
            area_texto.insert(END, "Disponivel\n", "disponivel")
        else:
            area_texto.insert(END, "Nao Disponivel\n", "indisponivel")

    def listar_livros_ui(self, area_texto):
        area_texto.delete('1.0', END)
        if not self.livros:
            area_texto.insert(END, "A biblioteca está vazia.", "rotulo")
            return
        for livro in self.livros:
            self.formatar_livro(area_texto, livro)

    def buscar_livro_ui(self, area_texto):
        dialogo = CTkInputDialog(text="Digite o nome do livro:", title="Buscar")
        busca = dialogo.get_input()

        if not busca: return

        area_texto.delete('1.0', END)
        encontrado = False
        for livro in self.livros:
            if busca.lower() in livro.titulo.lower():
                self.formatar_livro(area_texto, livro)
                encontrado = True

        if not encontrado:
            area_texto.insert(END, f"O livro '{busca}' não foi encontrado.", "indisponivel")

    def emprestar_livro_ui(self, area_texto):
        dialogo = CTkInputDialog(text="Nome do livro para emprestar:", title="Emprestar")
        busca = dialogo.get_input()

        if not busca: return

        for livro in self.livros:
            if livro.titulo.lower() == busca.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    self.salvar_dados()  # SALVA A ALTERAÇÃO DE STATUS
                    messagebox.showinfo("Sucesso", "Livro emprestado!")
                    self.listar_livros_ui(area_texto)
                else:
                    messagebox.showwarning("Aviso", "Este livro já está emprestado.")
                return
        messagebox.showerror("Erro", "Livro não encontrado.")

    def devolver_livro_ui(self, area_texto):
        dialogo = CTkInputDialog(text="Nome do livro para devolver:", title="Devolver")
        busca = dialogo.get_input()

        if not busca: return

        for livro in self.livros:
            if livro.titulo.lower() == busca.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    self.salvar_dados()  # SALVA A ALTERAÇÃO DE STATUS
                    messagebox.showinfo("Sucesso", "Livro devolvido!")
                    self.listar_livros_ui(area_texto)
                else:
                    messagebox.showwarning("Aviso", "O livro já estava disponível.")
                return
        messagebox.showerror("Erro", "Livro não encontrado.")


# --- Interface Principal ---
bib = Biblioteca()
janela = CTk()
janela.title('Sistema de Biblioteca - Adriano')
janela.geometry("1250x650")

frame_menu = CTkFrame(janela, width=200, corner_radius=0)
frame_menu.pack(side=LEFT, fill=Y, padx=0, pady=0)

CTkLabel(frame_menu, text='BIBLIOTECA', font=('Arial', 20, 'bold')).pack(pady=30, padx=20)

texto_display = Text(janela, font=("Consolas", 11), bg="#1e1e1e", fg="#ffffff", borderwidth=0, padx=15, pady=15)
texto_display.pack(side=RIGHT, expand=True, fill=BOTH, padx=20, pady=20)

texto_display.tag_configure("negrito", font=("Consolas", 11, "bold"), foreground="#ffffff")
texto_display.tag_configure("rotulo", foreground="#888888")
texto_display.tag_configure("disponivel", foreground="#2ecc71", font=("Consolas", 11, "bold"))
texto_display.tag_configure("indisponivel", foreground="#e74c3c", font=("Consolas", 11, "bold"))

btn_config = {"width": 180, "height": 40, "font": ("Arial", 12, "bold")}

CTkButton(frame_menu, text='➕ Adicionar Livro', command=lambda: bib.adicionar_livros_ui(texto_display),
          **btn_config).pack(pady=10)
CTkButton(frame_menu, text='📋 Listar Todos', command=lambda: bib.listar_livros_ui(texto_display), **btn_config).pack(
    pady=10)
CTkButton(frame_menu, text='🔍 Buscar Livro', command=lambda: bib.buscar_livro_ui(texto_display), **btn_config).pack(
    pady=10)
CTkButton(frame_menu, text='📤 Emprestar Livro', command=lambda: bib.emprestar_livro_ui(texto_display),
          **btn_config).pack(pady=10)
CTkButton(frame_menu, text='📥 Devolver Livro', command=lambda: bib.devolver_livro_ui(texto_display), **btn_config).pack(
    pady=10)

CTkButton(frame_menu, text='❌ Sair', command=janela.quit, fg_color="#c0392b", hover_color="#962d22", **btn_config).pack(
    side=BOTTOM, pady=30)

# Ao iniciar, já mostra os livros carregados do arquivo
janela.after(100, lambda: bib.listar_livros_ui(texto_display))

janela.mainloop()