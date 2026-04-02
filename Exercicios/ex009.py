velocidade = float(input('Digite a velocidade em Km/h: '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Esta dentro do limite')
else:
    print(f'Esta fora do limite terá que pagar uma multa de R${multa:.2f}')
