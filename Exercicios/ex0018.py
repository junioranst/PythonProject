frase = input('Digite uma frase: ').strip().lower().split()
nova_frase = ''.join(frase)
inverso = ''
print(nova_frase)
for l in range(len(nova_frase)-1, -1, -1):
    inverso += nova_frase[l]
print(inverso)
if inverso == nova_frase:
    print('Palindromo')
