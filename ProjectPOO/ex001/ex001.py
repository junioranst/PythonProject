
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
        livro_novo = Livro(titulo, autor, ano)

        self.livros.append(livro_novo)


    def listar_livros(self):
        for livro in self.livros:
            print(livro.titulo, livro.autor, livro.ano, livro.disponivel)


    def buscar_livro(self):
        busca = input('Digite o nome do livro: ').strip()
        for livro in self.livros:
            if livro.titulo.lower() == busca.lower():
                print(livro.titulo, livro.autor, livro.ano , livro.disponivel)

biblioteca = Biblioteca()

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
        biblioteca.adicionar_livros()


    elif escolha == '2':
        biblioteca.listar_livros()

    elif escolha == '3':
        biblioteca.buscar_livro()

    elif escolha == '4':


    elif escolha == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")

