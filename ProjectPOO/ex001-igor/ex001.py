# Exemplo básico de uma classe
from operator import truediv


class Livro:
    # O método __init__ é o construtor, chamado ao instanciar
    def __init__(self, titulo, autor, ano, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    # Método (funcionalidade)
    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

    def exibir_info(self):
        print(self.titulo, self.autor, self.ano, self.disponivel)

# # Instanciando a classe
# livro = Livro(titulo="", autor="", ano="")
# print(meu_carro.descrever())  # Saída: Toyota Corolla


class Biblioteca:
    # O método __init__ é o construtor, chamado ao instanciar
    def __init__(self): #lista de objetos Livro
        self.livros = []   # Atributo

    # Método (funcionalidade)
    def adicionar_livro(self):
        titulo = input("Digite o titulo: ")
        autor = input("Digite o autor: ")
        ano = input("Digite o ano: ")
        livro_novo = Livro(titulo, autor, ano)
        self.livros.append(livro_novo)

    def listar_livros(self):
        for livro in self.livros:
            print(livro.titulo, livro.autor, livro.ano, livro.disponivel)

    def buscar_livro(self):
        busca = input("Digite o titulo que você quer buscar: ")
        for livro in self.livros:
            if livro.titulo == busca:
                print(livro.titulo, livro.autor, livro.ano, livro.disponivel)

    def emprestar_livro(self, titulo):
        return


# Instanciando a classe
biblioteca = Biblioteca()


# Menu
def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Buscar livro")
    print("4. Emprestar livro")
    print("5. Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '1':
        biblioteca.adicionar_livro()

    elif escolha == '2':
        biblioteca.listar_livros()

    elif escolha == '3':
        biblioteca.buscar_livro()

    elif escolha == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")