numero = int(input('Digite um numero: '))
count = 0
for c in range(1, numero+1):
    if numero % c == 0:
        count += 1
if count == 2:
    print('\033[32mNumero primo\033[m')
else:
    print('\033[31mNao é primo\033[m')
