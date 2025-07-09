from cadastros.cadastropessoa import cadastroPessoa
from pessoa import Funcionario

def cadastroFuncionario():
    pessoa = cadastroPessoa("funcionário")
    cargo = input("Qual o seu cargo? ")
    cargahoraria = input("Qual a sua carga horária? ")
    funcionario = Funcionario(pessoa.idPessoa, pessoa.nomeCompleto, pessoa.CPF, cargo, cargahoraria)
    print(f"Funcionário {funcionario.nomeCompleto} cadastrado com sucesso.")