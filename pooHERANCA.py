#POO ERANCA

#cLASSE Animal
class Animal:
    def __init__(self, especie, cor):
        self.especie=especie
        self.cor=cor
    def obterEspecie(self):
        return  self.especie
    def obterCor(self):
        return  self.cor

class Mamifero(Animal):
    def __init__(self, cor_pelo):
        self.cor_pelo=cor_pelo
    def obterCorPelo(self):
        self.cor_pelo

class Felino(Mamifero):
    pass