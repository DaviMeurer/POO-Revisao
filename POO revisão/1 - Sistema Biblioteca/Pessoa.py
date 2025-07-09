#declarando que este arquivo é uma classe
class Pessoa:

    #outros atributos, função padrão construtor 
    def __init__(self, nome, endereco, telefone, 
                 idade, matricula):
        self.nome=nome
        self.endereco=endereco
        self.telefone=telefone
        self.idade=idade
        self.matricula=matricula
    

     #metodo - operação de alterar cadastro
    def alterarCadastro(self, end, tel, idade):
        self.endereco=end
        self.telefone=tel
        self.idade=idade


    #metodo - operação imprimir cadastro
    def imprimirCadastro(self):
        print(f"Nome: {self.nome}\n"+
              f"Matricula:{self.matricula}\n"
              f"Tel:{self.telefone}\n"
              f"Idade:{self.idade}\n"
              f"Endereço:{self.endereco}\n"
              )