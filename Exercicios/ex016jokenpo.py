import random
from time import sleep
while True:
    lista = ('pedra','papel','tesoura')
    escolha_pc = random.choice(lista)
    escolha_vc = input('Escolha pedra, papel ou tesoura: ').lower().strip()
    if escolha_vc in ('pedra','papel','tesoura'):
        print('JO')
        sleep(0.5)
        print('Ken')
        sleep(0.5)
        print('PO')
        sleep(0.5)
    if escolha_vc == 'pedra' and escolha_pc == 'papel':
        print(f'{escolha_pc} \033[031mVoce perdeu!\033[m')
    elif escolha_vc == 'pedra' and escolha_pc == 'pedra':
        print(f'{escolha_pc} \033[033mDeu empate!\033[m')
    elif escolha_vc == 'pedra' and escolha_pc == 'tesoura':
        print(f'{escolha_pc} \033[032mVoce ganhou!\033[m')
    elif escolha_vc == 'papel' and escolha_pc == 'pedra':
        print(f'{escolha_pc} \033[032mVoce ganhou!\033[m')
    elif escolha_vc == 'papel' and escolha_pc == 'papel':
        print(f'{escolha_pc} \033[033mDeu empate!\033[m')
    elif escolha_vc == 'papel' and escolha_pc == 'tesoura':
        print(f'{escolha_pc} \033[031mVoce perdeu!\033[m')
    elif escolha_vc == 'tesoura' and escolha_pc == 'pedra':
        print(f'{escolha_pc} \033[031mVoce perdeu!\033[m')
    elif escolha_vc == 'tesoura' and escolha_pc == 'papel':
        print(f'{escolha_pc} \033[032mVoce ganhou!\033[m')
    elif escolha_vc == 'tesoura' and escolha_pc == 'tesoura':
        print(f'{escolha_pc} \033[033mDeu empate!\033[m')
    else:
        break
