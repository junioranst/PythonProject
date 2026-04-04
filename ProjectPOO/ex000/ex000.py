class carro:
    def __init__(self):
        #Atributos da Instancia
        self.marca = ''
        self.modelo = ''
        self.kilometragem = 0
    #20,832
    # Métodos da Instancia
    def nurburgring(self):
        self.kilometragem += 20832

    def spa_francorchamps(self):
        self.kilometragem += 7004

    def mensagem(self):
        return f'o modelo do carro é {self.marca}, modelo {self.modelo} e percorreu {self.kilometragem} Km'

car1 = carro()
car1.marca = 'Ferrari'
car1.modelo = '296 Gt3'
car1.kilometragem = 1000
car1.nurburgring()
print(car1.mensagem())

car2 = carro()
car2.marca = 'Porche'
car2.modelo = 'Gt3 RS'
car2.kilometragem = 45000
car2.spa_francorchamps()
print(car2.mensagem())

car3 = carro()
car3.marca = 'BMW'
car3.modelo = 'M4 Gt3'
car3.kilometragem = 7000
car3.spa_francorchamps()
car3.nurburgring()
print(car3.mensagem())
