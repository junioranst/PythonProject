s = cont = 0
while True:
    n = int(input('Digite um numero\033[1;37m(ou 999 para parar)\033[m:'))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos numeros é de: \033[1;34m{s}\033[m e foram digitados \033[1;34m{cont}\033[m numeros.')