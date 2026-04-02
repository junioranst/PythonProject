import matplotlib.pyplot as plt


class livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.titulo}, Autor: {self.autor}, Genero: {self.genero}, Quantidade: {self.quantidade}'


biblioteca = []


def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    quantidade = int(input("Digite a quantidade do livro: "))
    novo_livro = livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print("Livro adicionado com sucesso!\n")


def listar_livros():
    print("Lista de Livros:")
    for livro in biblioteca:
        print(livro)


def buscar_livro():
    titulo_busca = input("Digite o título do livro que deseja buscar: ")
    encontrados = [livro for livro in biblioteca if livro.titulo.lower() == titulo_busca.lower()]

    if encontrados:
        print("Livro(s) encontrado(s):")
        for livro in encontrados:
            print(livro)
    else:
        print("Nenhum livro encontrado com esse título.")


def grafico_generos():
    if not biblioteca:
        print("Nenhum livro cadastrado para gerar gráfico.")
        return

    # Contar quantidade de livros por gênero
    generos = {}
    for livro in biblioteca:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade
        else:
            generos[livro.genero] = livro.quantidade

    # Preparar dados
    nomes = list(generos.keys())
    quantidades = list(generos.values())

    # Criar gráfico de barras
    plt.bar(nomes, quantidades, color='royalblue')
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de Livros")
    plt.title("Quantidade de Livros por Gênero")
    plt.show()


# Menu principal
while True:
    print("\nMenu:")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro pelo título")
    print("4 - Gerar gráfico por gênero")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livro()
    elif opcao == "4":
        grafico_generos()
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")