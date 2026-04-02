v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
print('-='*20)
print('Menu'.center(40))
print('-='*20)
print('1 - Somar')
print('2 - Multiplicar')
print('3 - Maior')
print('4 - Novos numeros')
print('5 - Sair')
print('-='*20)
while True:
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        print(f'A soma é igual a: {v1 + v2}')
        print('-=' * 20)
    elif escolha == 2:
        print(f'A multiplicacao é igual a: {v1 * v2}')
        print('-=' * 20)
    elif escolha == 3:
        if v1 > v2:
            print(f'O maior numero é {v1}')
            print('-=' * 20)
        else:
            print(f'O maior numero é {v2}')
            print('-=' * 20)
    elif escolha == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
        print('-=' * 20)
    elif escolha == 5:
        break
    else:
        print('Opcao invalida!')




