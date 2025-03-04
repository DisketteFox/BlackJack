class Carta:
    def __init__(self, palo, valor, nombre):
        self.palo = palo
        self.valor = valor
        self.nombre = nombre
    def __str__(self):
        return f"{self.nombre}"