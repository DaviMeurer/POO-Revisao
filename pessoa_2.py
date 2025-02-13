
class Pessoa:
    def __init__(self,idPessoa,nomeCompleto,CPF):
        self.idPessoa = idPessoa
        self.nomeCompleto = nomeCompleto
        self.CPF = CPF

class Funcionario(Pessoa):
    def __init__(self, idPessoa, nomeCompleto, CPF,cargo,cargahoraria):
        super().__init__(idPessoa, nomeCompleto, CPF)
        self.cargo = cargo
        self.cargahoraria = cargahoraria

class Cliente(Pessoa):
    def __init__(self, idPessoa, nomeCompleto, CPF,nivelCliente,gerente):
        super().__init__(idPessoa, nomeCompleto, CPF)
        self.nivelCliente = nivelCliente
        self.gerente = gerente
