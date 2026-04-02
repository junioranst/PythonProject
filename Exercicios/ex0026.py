print('-' * 40)
n = int(input('Digite um numero: '))
print('-'*40)
tabuada = 1
while tabuada <= 10:
    print(f'{n} x {tabuada} = {n * tabuada}')
    tabuada += 1
    if tabuada > 10:
        print('-' * 40)
        n = int(input('Digite um numero: '))
        print('-' * 40)
        tabuada = 1
    if n < 0:
        break