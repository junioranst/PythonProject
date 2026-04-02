def binario(n):
    binario_str = ""
    while n > 0:
        resto = n % 2
        binario_str = str(resto) + binario_str
        n = n // 2
    return binario_str
# Teste
n = 2
print(binario(n))

bina = (bin(n))
print(bina[2:])