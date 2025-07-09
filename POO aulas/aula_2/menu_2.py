import time

from cadastros.cadastrocliente import cadastroCliente
from cadastros.cadastrofuncionario import cadastroFuncionario


def mostraMenu():

    while True:
        print("Digite a opção desejada:")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Funcionário")
        print("3 - Sair do programa")
        opt=input()
        match opt:
            case '1':
                cadastroCliente()
            case '2':
                cadastroFuncionario()
            case '3':
                print("saindo do programa ...")
                time.sleep(1)
                break
            case _:
                print("Opção inválida. Tente novamente")
