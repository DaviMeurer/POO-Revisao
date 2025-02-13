class veiculo:
    def __init__(self, modelo, roda, cor, marca):
        self.modelo = modelo
        self.roda = roda
        self.cor = cor
        self.marca = marca

class carro(veiculo):
    def __init__(self, modelo, roda, cor, marca, porta):
        super().__init__(modelo, roda, cor, marca)
        self.porta = porta
        
    def registrarCarro(self):
        print (f"O carro {self.modelo} da marca {self.marca} que possui {self.roda} rodas e {self.porta} {self.cor} foi registrado com sucesso!")

class moto(veiculo):
    def __init__(self, modelo, roda, cor, marca, cilindrada):
        super().__init__(modelo, roda, cor, marca)
        self.cilindrada = cilindrada
        
    def registrarMoto(self):
        print (f"A moto {self.modelo} da marca {self.marca} que possui {self.roda} rodas {self.cor} foi registrado com sucesso!")