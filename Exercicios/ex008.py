from random import randint
from time import sleep
numero = randint(0,5)
escolha = int(input('Escolha um numero entre 0 e 5: '))
print('Loading...')
sleep(3)
if escolha == numero:
    print(f'Parabens certa resposta o numero é {numero}')
else :
    print(f'Voce errou o numero é {numero}')
