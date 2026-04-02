

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = float(input('Digite em quantos anos pretende pagar: '))
prestacao = valor_casa / (anos * 12)
porcentagem = (salario / 100) * 30

if prestacao > porcentagem:
    print('Empréstimo \033[97;41m Negado \033[m')
    print(f'O valor da prestaçao corresponde a R$\033[4;31m{prestacao:.2f}\033[m')
    print(f'Valor este que excede a 30% do seu salário que é de R$\033[97;41m{porcentagem:.2f}\033[m')
else:
    print('Empréstimo \033[97;42m Aprovado \033[m')
    print(f'O valor da prestaçao corresponde a R$\033[4;32m{prestacao:.2f}\033[m')
    print(f'O valor nao excede a 30% do seu salário que é de R$\033[97;42m{porcentagem:.2f}\033[m')
