class carro:
    """Esta clase cria o objeto carro"""
    def __init__(self, marca = '', modelo = '', kilometragem = 0):
        #Atributos da Instancia
        self.marca = marca
        self.modelo = modelo
        self.kilometragem = kilometragem
    #20,832
    # Métodos da Instancia
    def nurburgring(self):
        self.kilometragem += 20832

    def spa_francorchamps(self):
        self.kilometragem += 7004

    def __str__(self):
        return f'A marca do carro é {self.marca}, modelo {self.modelo} e percorreu {self.kilometragem} Km'
    def __getstate__(self):
        return f'Estado: {self.marca}, modelo {self.modelo}, distancia {self.kilometragem} Km'


car1 = carro('Ferrari','296 Gt3', 1000)
car1.nurburgring()
print(car1)

car2 = carro('Porche','Gt3 RS',45000)
car2.spa_francorchamps()
print(car2)

car3 = carro('BMW','M4 Gt3',7000)
car3.spa_francorchamps()
car3.nurburgring()
print(car3)
print(car1.__doc__)
print(car2.__getstate__())
print(car3.__class__)