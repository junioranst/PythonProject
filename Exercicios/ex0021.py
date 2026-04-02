pt = int(input('escreva o primeiro termo: '))
razao = int(input('escreva a razao: '))
cont = 1
n1 = pt
novostermos = 10
total = 0

while novostermos != 0:
    total = total + novostermos
    while cont <= total:
        n1 = n1 + razao
        print(n1 - razao, end=' ')
        print('>' if cont < 10 else '', end=' ')
        cont += 1
    novostermos = int(input('gostaria de ver mais quantos termos? : '))
