print('=' * 30)
print(f'{"BANCO DO PAI":^30}')
print('=' * 30)

valor = int(input("Digite um valor: "))
notas = [50, 20, 10, 1]

print('Notas entregues:')

for nota in notas:
    quantidade = valor // nota
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R${nota}")
    valor %= nota
