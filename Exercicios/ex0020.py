numero = int(input('Digite um numero: '))
fac = 1
while numero > 0:
    fac *= numero
    print(f'{numero}', end=' ')
    print('x' if numero > 1 else '=', end=' ')
    numero -= 1
print(fac)
