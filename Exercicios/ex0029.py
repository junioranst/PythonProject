total = 0
acima1k = 0
nome = input('Digite o nome do produto: ').strip()
valor = float(input('Digite o Valor do produto: '))
menor = valor
barato = nome
while True:

    total += valor
    if valor > 1000:
        acima1k += 1

    if valor < menor:
        menor = valor
        barato = nome
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break

    if continuar == 'N':
        break

    nome = input('Digite o nome do produto: ').strip()
    valor = float(input('Digite o Valor do produto: '))

print('-='*35)
print(f'total gasto na compra foi de: R${total}')
print(f'A quantidade de produtos que ficaram acima de Mil Reais foi de: {acima1k}')
print(f'O produto mais barato foi: {barato}')