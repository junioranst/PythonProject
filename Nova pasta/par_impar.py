import random
vitoria = 0
print('\033[1;33m-=\033[m'*30)
print('\033[1;97mJogo do Par ou Impar\033[m'.center(70))
print('\033[1;33m-=\033[m'*30)
while vitoria == 0:

    numero = int(input('Digite um numero: '))
    escolha = (input('Escolha par ou impar: '))
    numeropc = random.randint(0,100)

    resposta = (numero + numeropc) % 2
    if resposta == 0:
        resposta = 'par'
    else:
        resposta = 'impar'

    if escolha == resposta:
        print(f'Eu escolho {numeropc}')
        print(f'Parabens {numero + numeropc} da\033[1;92m {resposta}\033[m!')
        vitoria += 1
    else:
        print(f'Eu escolho {numeropc}')
        print(f'Voce errou {numero + numeropc} da\033[1;91m {resposta}\033[m!')
        print('\033[1;33m-=\033[m' * 30)



