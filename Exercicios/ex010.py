a = float(input('Digite o lado A: '))
b = float(input('Digite o lado B: '))
c = float(input('Digite o lado C: '))
if  (a + b > c and a + c > b and b + c > a):
    print('Triangulo: \033[97;42m Possivel \033[m')
    if (a == b == c):
        print('Triangulo Equilátero')
    elif (a == b or b == c or c == a):
        print('Triangulo Isoceles')
    elif (a != b and b != c and c != a):
        print('Triangulo Escaleno')

else:
    print('Triangulo: \033[97;41m Impossivel \033[m')
