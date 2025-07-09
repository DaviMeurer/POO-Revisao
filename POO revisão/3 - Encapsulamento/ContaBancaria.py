class ContaBancaria:
    def __init__(self, titular, saldo=0) -> None:
        self.titular=titular
        self.__saldo=saldo  #atrubuto privado, acessivel só aqui na classe


    def __alteraSaldo(self, saldo): #metodo privado, acessivel só aqui na clase
        self.__saldo=saldo

    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        if valor>0:
            self.__saldo=valor
        else:
            print ("Não é permitido saldo negativo!")