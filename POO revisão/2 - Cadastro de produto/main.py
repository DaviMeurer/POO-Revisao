from Produto import Produto

while(True):
    print("BEM VINDO AO SISTEMA DE PRODUTOS")
    print("Escolha uma opção:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Alterar")
    print("4 - Excluir")
    print("0 - Sair")
    escolha = input("Digite: ")

    match escolha:
        case 1:
          print("Opção 1")
        case 0:
          print("bye (>‿◠)✌")
        case _:
          print("Opção Inválida!")
   