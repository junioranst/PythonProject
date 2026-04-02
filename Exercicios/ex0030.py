print('='*30)
print(f'{"BANCO DO PAI":^30}')
print('='*30)
valor = int(input("Digite um valor: "))
cinquenta = 0
vinte = 0
dez = 0
um = 0

while valor > 0:
    if valor >= 50:
        cinquenta = valor // 50
        valor = valor - (cinquenta * 50)
    if valor >= 20:
        vinte = valor // 20
        valor = valor - (vinte * 20)
    if valor >= 10:
        dez = valor // 10
        valor = valor - (dez * 10)
    if valor >= 1:
        um = valor // 1
        valor = valor - (um * 1)

if cinquenta > 0:
    print(f'Notas de Cinquenta: {cinquenta}')
if vinte > 0:
    print(f'Notas de Vinte: {vinte}')
if dez > 0:
    print(f'Notas de Dez: {dez}')
if um > 0:
    print(f'Notas de Um: {um}')
