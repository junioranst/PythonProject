from abc import ABC, abstractmethod
import math
class Poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, tam_lado=0):
        super().__init__(4)
        self.tam_lado = tam_lado

    def perimetro(self):
        perimetro = (self.tam_lado * self.qtd_lados)
        return f'O quadrado um perimetro de: {perimetro:.2f} '

    def area(self):
        area = (self.tam_lado * self.tam_lado)
        return f'O quadrado possui uma area de: {area:.2f}'


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio
        self.pi = math.pi
    def perimetro(self):
        perimetro = ((self.pi * 2) * self.raio)
        return f'O circulo possui um perimetro de: {perimetro:.2f} '

    def area(self):
        area = (self.pi *(self.raio ** 2))
        return f'O circulo possui uma area de: {area:.2f}'














