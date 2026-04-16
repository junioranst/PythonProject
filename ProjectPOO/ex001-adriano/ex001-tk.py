from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter.font import BOLD

from customtkinter import *

class Livro:
    def __init__(self,titulo,autor,ano,disponivel=True ):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def emprestar(self):
        self.disponivel = False
    def devolver(self):
        self.disponivel = True
    def exibir_info(self):
        print(self.titulo)
        print(self.autor)
        print(self.ano)
        print(self.disponivel)

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livros(self):
        titulo = input('Digite o titulo do livro: ').strip()
        autor = input('Digite o autor do livro: ').strip()
        ano = input('Digite o ano do livro: ').strip()

        self.livros.append(Livro(titulo, autor, ano))
        print(f'O livro {titulo} foi adicionado com sucesso na biblioteca!')

    def listar_livros(self):
        for livro in self.livros:
            print(f'Titulo: \033[1;97m{livro.titulo}\033[m | Autor: \033[1;97m{livro.autor}\033[m | Ano: '
                  f'\033[1;97m{livro.ano}\033[m | 'f'Livro: {'\033[1;32mDisponivel\033[m' if livro.disponivel 
            else '\033[1;31mNao Disponivel\033[m' }')


    def buscar_livro(self):
        busca = input('Digite o nome do livro: ').strip()
        for livro in self.livros:
            if livro.titulo.lower() == busca.lower():
                print(f'Titulo: \033[1;97m{livro.titulo}\033[m | Autor: \033[1;97m{livro.autor}\033[m | Ano: '
                      f'\033[1;97m{livro.ano}\033[m | 'f'Livro: {'\033[1;32mDisponivel\033[m' if livro.disponivel
                else '\033[1;31mNao Disponivel\033[m'}')
                return
        print(f'O livro {busca} nao foi encontrado na biblioteca')

    def emprestar_livro(self):
        busca = input('Digite o nome do livro que deseja emprestar: ').strip()
        for livro in self.livros:
            if livro.titulo.lower() == busca.lower():
                if livro.disponivel:
                    livro.emprestar()
                    print(f'O livro {livro.titulo} foi emprestado com sucesso!')
                else:
                    print('O livro ja foi emprestado')
                return
        print('Livro nao encontrado')

    def devolver_livro(self):
        busca = input('Digite o nome do livro que deseja devolver: ').strip()
        for livro in self.livros:
            if livro.titulo.lower() == busca.lower():
                if not livro.disponivel:
                    livro.devolver()
                    print(f'O livro {livro.titulo} foi devolvido com sucesso!')
                else:
                    print('O livro ja foi devolvido')
                return
        print('Livro nao encontrado')



biblioteca = Biblioteca()

#def mostrar_menu():
    #print("\n--- MENU ---")
    #print("1. Adicionar livro")
    #print("2. Listar livros")
    #print("3. Buscar livro")
    #print("4. Emprestar livro")
    #print("5. Devolver livro")
    #print("6. Sair")

#while True:
    #mostrar_menu()
    #escolha = (input('Escolha uma opção (1-6): '))

    #if escolha == '1':
        #biblioteca.adicionar_livros()

    #elif escolha == '2':
        #biblioteca.listar_livros()

    #elif escolha == '3':
        #biblioteca.buscar_livro()

    #elif escolha == '4':
        #biblioteca.emprestar_livro()

    #elif escolha == '5':
        #biblioteca.devolver_livro()

    #elif escolha == '6':
        #print("Saindo...")
        #break
    #else:
        #print("Opção inválida, tente novamente.")

#Tkinter
janela = CTk()
janela.title('Biblioteca do Adriano')
janela.geometry("900x550")

menu_lateral = CTkFrame(janela, width=200, corner_radius=0)
menu_lateral.pack(side=LEFT, fill=Y, padx=0, pady=0)

CTkLabel(menu_lateral, text='Biblioteca', font=('Arial',30,BOLD)).pack(pady=30, padx=20)

CTkButton(menu_lateral, text='Adicionar Livro').pack(pady=10)

janela.mainloop()