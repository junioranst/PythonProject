altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em quilo: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'seu imc é {imc:.2f}: Voce está abaixo do peso!')
elif 18.5 <= imc < 25:
    print(f'seu imc é {imc:.2f}: Voce está no peso ideal!')
elif 25 <= imc < 30:
    print(f'seu imc é {imc:.2f}: Voce está com sobrepeso!')
elif 30 <= imc <= 40:
    print(f'seu imc é {imc:.2f}: Voce está é obeso gordo pra carai!')
else:
    print(f'seu imc é {imc:.2f}: Voce está com obesidade morbida baleia')