a = -1
b = 6
c = -9

def baskara(a, b, c):
    delta = b**2 - 4*a*c
    x = (-b + delta**0.5)/(2*a)
    y = (-b - delta**0.5)/(2*a)
    return x, y

print(baskara(a, b, c))
