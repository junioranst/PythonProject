import tkinter as tk
from tkinter import messagebox, simpledialog


class Livro:
    def __init__(self, titulo, autor, ano, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livros_ui(self, area_texto):
        self.janela_add = tk.Toplevel()
        self.janela_add.title("Cadastrar Novo Livro")
        self.janela_add.geometry("300x200")

        tk.Label(self.janela_add, text="Título:").grid(row=0, column=0, padx=10, pady=5)
        ent_titulo = tk.Entry(self.janela_add)
        ent_titulo.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.janela_add, text="Autor:").grid(row=1, column=0, padx=10, pady=5)
        ent_autor = tk.Entry(self.janela_add)
        ent_autor.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.janela_add, text="Ano:").grid(row=2, column=0, padx=10, pady=5)
        ent_ano = tk.Entry(self.janela_add)
        ent_ano.grid(row=2, column=1, padx=10, pady=5)

        def salvar():
            t, aut, ano = ent_titulo.get().strip(), ent_autor.get().strip(), ent_ano.get().strip()
            if t and aut and ano:
                self.livros.append(Livro(t, aut, ano))
                self.janela_add.destroy()
                self.listar_livros_ui(area_texto)  # Atualiza a lista automaticamente
                messagebox.showinfo("Sucesso", f"O livro '{t}' foi adicionado!")
            else:
                messagebox.showwarning("Erro", "Preencha todos os campos!")

        tk.Button(self.janela_add, text="Salvar Livro", command=salvar, bg="#4CAF50", fg="white").grid(row=3,
                                                                                                       columnspan=2,
                                                                                                       pady=15)

    def formatar_livro(self, area_texto, livro):
        """Função auxiliar para imprimir o livro com o seu estilo original"""
        area_texto.insert(tk.END, "Titulo: ", "rotulo")
        area_texto.insert(tk.END, f"{livro.titulo} ", "negrito")
        area_texto.insert(tk.END, "| Autor: ", "rotulo")
        area_texto.insert(tk.END, f"{livro.autor} ", "negrito")
        area_texto.insert(tk.END, "| Ano: ", "rotulo")
        area_texto.insert(tk.END, f"{livro.ano} ", "negrito")
        area_texto.insert(tk.END, "| Livro: ", "rotulo")

        if livro.disponivel:
            area_texto.insert(tk.END, "Disponivel\n", "disponivel")
        else:
            area_texto.insert(tk.END, "Nao Disponivel\n", "indisponivel")

    def listar_livros_ui(self, area_texto):
        area_texto.delete('1.0', tk.END)
        if not self.livros:
            area_texto.insert(tk.END, "A biblioteca está vazia.", "rotulo")
            return
        for livro in self.livros:
            self.formatar_livro(area_texto, livro)

    def buscar_livro_ui(self, area_texto):
        busca = simpledialog.askstring("Buscar", "Digite o nome do livro:")
        if not busca: return

        area_texto.delete('1.0', tk.END)
        encontrado = False
        for livro in self.livros:
            if busca.lower() in livro.titulo.lower():
                self.formatar_livro(area_texto, livro)
                encontrado = True

        if not encontrado:
            area_texto.insert(tk.END, f"O livro '{busca}' não foi encontrado.", "indisponivel")

    def emprestar_livro_ui(self, area_texto):
        busca = simpledialog.askstring("Emprestar", "Nome do livro para emprestar:")
        if not busca: return

        for livro in self.livros:
            if livro.titulo.lower() == busca.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    messagebox.showinfo("Sucesso", "Livro emprestado!")
                    self.listar_livros_ui(area_texto)
                else:
                    messagebox.showwarning("Aviso", "Este livro já está emprestado.")
                return
        messagebox.showerror("Erro", "Livro não encontrado.")

    def devolver_livro_ui(self, area_texto):
        busca = simpledialog.askstring("Devolver", "Nome do livro para devolver:")
        if not busca: return

        for livro in self.livros:
            if livro.titulo.lower() == busca.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    messagebox.showinfo("Sucesso", "Livro devolvido!")
                    self.listar_livros_ui(area_texto)
                else:
                    messagebox.showwarning("Aviso", "O livro já estava disponível.")
                return
        messagebox.showerror("Erro", "Livro não encontrado.")


# --- Interface Principal ---
bib = Biblioteca()
janela = tk.Tk()
janela.title('Sistema de Biblioteca - Adriano')
janela.geometry("850x500")
janela.configure(bg="#2d2d2d")  # Fundo da janela principal

# Menu Lateral
frame_menu = tk.Frame(janela, bg="#2d2d2d")
frame_menu.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

tk.Label(frame_menu, text='BIBLIOTECA', font=('Arial', 14, 'bold'), bg="#2d2d2d", fg="white").pack(pady=10)

# Área de Texto (Onde a mágica visual acontece)
texto_display = tk.Text(janela, font=("Consolas", 11), bg="#1e1e1e", fg="#ffffff", padx=10, pady=10)
texto_display.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=20)

# Configuração de Cores e Estilos (Tags)
texto_display.tag_configure("negrito", font=("Consolas", 11, "bold"), foreground="#ffffff")
texto_display.tag_configure("rotulo", foreground="#888888")
texto_display.tag_configure("disponivel", foreground="#00ff00", font=("Consolas", 11, "bold"))
texto_display.tag_configure("indisponivel", foreground="#ff4444", font=("Consolas", 11, "bold"))

# Botões do Menu
estilo_btn = {"width": 22, "pady": 8, "font": ("Arial", 10, "bold"), "cursor": "hand2"}

tk.Button(frame_menu, text='➕ Adicionar Livro', command=lambda: bib.adicionar_livros_ui(texto_display),
          **estilo_btn).pack(pady=4)
tk.Button(frame_menu, text='📋 Listar Todos', command=lambda: bib.listar_livros_ui(texto_display), **estilo_btn).pack(
    pady=4)
tk.Button(frame_menu, text='🔍 Buscar Livro', command=lambda: bib.buscar_livro_ui(texto_display), **estilo_btn).pack(
    pady=4)
tk.Button(frame_menu, text='📤 Emprestar Livro', command=lambda: bib.emprestar_livro_ui(texto_display),
          **estilo_btn).pack(pady=4)
tk.Button(frame_menu, text='📥 Devolver Livro', command=lambda: bib.devolver_livro_ui(texto_display), **estilo_btn).pack(
    pady=4)

# Botão Sair
tk.Button(frame_menu, text='❌ Sair', command=janela.quit, bg="#cc0000", fg="white", **estilo_btn).pack(pady=30)

janela.mainloop()