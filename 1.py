class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

mi_base = 10
mi_altura = 5
rect = Rectangulo(mi_base, mi_altura)
area_calculada = rect.calcular_area()
print(f"El área del rectángulo es: {area_calculada}")
