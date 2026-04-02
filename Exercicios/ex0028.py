continuar = 'S'
maior18 = homem = mulher20 = 0
while continuar == 'S':
    idade = int(input('Idade: '))
    sexo = (input('Sexo: [M/F]: ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).upper()
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    continuar = input('Deseja continuar? [S/N]: ').upper()
    while continuar not in 'NS':
        continuar = input('Deseja continuar? [S/N]: ').upper()


print(f'Maiores de idade: {maior18}')
print(f'Homens: {homem}')
print(f'Mulher abaixo de 20: {mulher20}')