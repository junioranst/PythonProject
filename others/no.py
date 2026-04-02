class Computador:
    def __init__(self, marca, processador, placa_video, memoria):
        self.marca = marca
        self.processador = processador
        self.placa_video = placa_video
        self.memoria = memoria
computador1 = Computador('Asus Prime','Ryzen 5 5600x','AMD rx6750xt','32Gb')
computador2 = Computador('Positivo','Intel Pentium','AMD rx 8000','16Gb')
computador3 = Computador('Apple','Intel Core 9','RTX 4060ti','8Gb')
computador4 = Computador('Acer','Ryzen 9','AMD rx 7500','64Gb')
print(computador1.memoria,computador1.processador,computador1.placa_video,computador1.memoria)
print(computador2.memoria,computador2.processador,computador2.placa_video,computador2.memoria)
print(computador3.memoria,computador3.processador,computador3.placa_video,computador3.memoria)
print(computador4.memoria,computador4.processador,computador4.placa_video,computador4.memoria)



