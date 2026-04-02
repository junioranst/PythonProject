n = int(input('digite um numero inteiro: '))
count = total = 0
while n!=999:
    count += 1
    total += n
    n = int(input('digite um numero inteiro: '))
print(f'Voce digitou \033[1;31m{count}\033[m numeros e o total dos numeros foi de \033[1;31m{total}\033[m')