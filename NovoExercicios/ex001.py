vendas = [
    {"produto": "Notebook", "preco": 3500, "quantidade": 2},
    {"produto": "Mouse", "preco": 80, "quantidade": 10},
    {"produto": "Teclado", "preco": 150, "quantidade": 5},
    {"produto": "Monitor", "preco": 900, "quantidade": 3}
]

def calcular_faturamento(vendas):
    total = 0
    for venda in vendas:
        total += venda['preco'] * venda['quantidade'] #total = total + vendas
    return total

def produto_mais_vendido(vendas):
    mais_vendido = 0
    nome_mais_vendido = ''
    for venda in vendas:
        if venda['quantidade'] > mais_vendido:
            mais_vendido = venda['quantidade']
            nome_mais_vendido = venda['produto']
    return nome_mais_vendido

def produto_maior_receita(vendas):
    maior_receita = 0
    nome_maior_receita = ''
    for venda in vendas:
        if venda['preco'] * venda['quantidade'] > maior_receita:
            maior_receita = venda['preco'] * venda['quantidade']
            nome_maior_receita = venda['produto']
    return nome_maior_receita, maior_receita

valor_minimo = 1000
def produtos_caros(vendas, valor_minimo):
    lista_caros = []
    for venda in vendas:
        if venda['preco'] > valor_minimo:
            lista_caros.append(venda['produto'])
    return lista_caros


def main():
    print(f'O faturamento total foi de:\n\033[1;97m- R${calcular_faturamento(vendas)}\033[m')
    print(f'O produto mais vendido foi:\n\033[1;97m- {produto_mais_vendido(vendas)}\033[m')
    nome, valor = produto_maior_receita(vendas)
    print(f'O produto que gerou mais receita foi:\n\033[1;97m- {nome} com R${valor} no total\033[m')
    print(f'Os Produtos acima de R$1.000 sao: ')
    for produto in produtos_caros(vendas, valor_minimo):
        print(f'\033[1;97m- {produto}\033[m')

main()