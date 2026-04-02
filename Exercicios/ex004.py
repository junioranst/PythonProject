while True:
    print('0 - Para finalizar')
    print('1 - Km')
    print('2 - Hm')
    print('3 - Dam')
    print('4 - M')
    print('5 - Dm')
    print('6 - Cm')
    unidade = int(input('Escolha a unidade de medida: '))


    if unidade == 0:
        break
    elif unidade == 1:
        km = int(input('Digite o valor em Km: '))
        print(f'A conversao do valor fica: {km}km \n{km * 10}hm \n{km * 100}dam \n{km * 1000}m \n{km * 10000}dm \n{km * 100000}cm \n{km * 1000000}mm')

    


