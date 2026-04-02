print(f'{"Loja Junioran":=^40}')
print('-'*40)
valor_produto = float(input('Digite o valor do produto: R$'))
forma_pagamento = int(input('''Forma de pagamento: 
1 - Dinheiro 
2 - Cartao 
3 - cheque
Digite sua opcao: '''))
parcelas = int(input('Digite a quantidade de parcelas: '))

if forma_pagamento in (1, 3) and parcelas == 1:
    print(f'O valor a vista sera de R${valor_produto - (valor_produto * 10 / 100):.2f}')
    print('10% de desconto aplicado')
elif parcelas == 1 and forma_pagamento == 2:
    print(f'O valor a vista sera de R${valor_produto - (valor_produto * 5 / 100):.2f}')
    print('5% de desconto aplicado')
elif parcelas == 2 and forma_pagamento == 2:
    print(f'O valor será de 2 parcelas de R${valor_produto / parcelas:.2f}')
    print(f'Sem desconto aplicado aplicado, valor total R${valor_produto:.2f}')
elif parcelas >= 3 and forma_pagamento == 2:
    print(f'O valor será de {parcelas} parcelas de R${(valor_produto + (valor_produto * 20 / 100)) / parcelas:.2f}')
    print(f'O valor total será de R${valor_produto + (valor_produto * 20 / 100):.2f} com 20% de juros')
else:
    print('Modo de pagamento nao valido')

