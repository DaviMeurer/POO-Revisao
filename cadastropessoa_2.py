from pessoa import Pessoa

def cadastroPessoa(tipopessoa):
    id = input(f"digite o id do {tipopessoa}: ")
    nomeCompleto = input(f"digite o nome completo do {tipopessoa}: ")
    cpf=input(f"digite o cpf do {tipopessoa}: 3")
    pessoa = Pessoa(id,nomeCompleto,cpf)
    return pessoa