#Classe pai
class animal:
    def __init__(self, raca, cor, dieta):
        self.raca = raca
        self.cor = cor
        self.dieta = dieta

#Classes filhos
class gato(animal): 
    def __init__(self, raca, cor, dieta, domesticado):
        super().__init__(raca, cor, dieta)
        self.domesticado = domesticado

    def brincar(self): #método brincar
        return "Brincando Junto"

class tigre(animal):
    def __init__(self, raca, cor, dieta, domado):
        super().__init__(raca, cor, dieta)
        self.domado = domado
    
    def atuar_junto(self):
        return "Atuando Junto"