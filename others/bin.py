def binario(x):
  bina1 = bin(x)
  return(bina1)

def bina(y):
  binar = ''
  while y > 0:
    resto = y % 2
    binar = str(resto) + binar
    y = y // 2
  return(binar)

while True:
  print('Menu\n')
  print('press 1 to Python bin')
  print('press 2 to Adriano bin')
  print('press 3 to break')
  comand = input('select yout option: ')

  if comand == '1':
    x = int(input('type a number: '))
    print(binario(x))

  elif comand == '2':
    y = int(input('type a number: '))
    print(bina(y))
  elif comand == '3':
    print('Ending program...')
    break


