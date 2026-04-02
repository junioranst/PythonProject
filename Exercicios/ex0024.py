n = int(input('Digite um numero inteiro: '))
simounao = (input('Quer continuar? [S/N] : ')).upper().strip()[0]
count = 1
lista = list()
lista.append(n)
while simounao == 'S':
    n = int(input('Digite um numero inteiro: '))
    lista.append(n)
    simounao = (input('Quer continuar? [S/N] : ')).upper().strip()
    count += 1
media = sum(lista) / count
maior = max(lista)
menor = min(lista)
print(f'A média foi de {media}, O maior numero foi de {maior} e o menor numero foi de {menor}')


