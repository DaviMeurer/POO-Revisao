from cadastros.cadastropessoa import cadastroPessoa
from pessoa import Cliente

def cadastroCliente():
    pessoa = cadastroPessoa("cliente")
    nivelcliente = input("Digite o nível do cliente: ")
    gerente = input ("Digite o nome do gerente responsável por esse cliente: ")
    cliente = Cliente(pessoa.idPessoa,pessoa.nomeCompleto,pessoa.CPF,nivelcliente,gerente)
    print(f"cliente {cliente.nomeCompleto} cadastrado com sucesso")