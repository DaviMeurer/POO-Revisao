from Pessoa import Pessoa

#criar um objeto
pessoa1 = Pessoa("Joao Dev", "Av. Brasil, n800",
                  "67999999", 25, 45200)
pessoa2 = Pessoa("Pedro Designer", "Marechal Floriano, n 155",
                  "67999999", 22, 45201)

#imprimir o tipo da variavel pessoa1
print(type(pessoa1))
#Acessando a informação do objeto
print(pessoa1.nome)
print(pessoa2.nome)

pessoa1.imprimirCadastro()
print("------------------")
pessoa2.imprimirCadastro()


#alterar informacao do pessoa2
pessoa2.alterarCadastro("7 de setembro, n 679",
                         "6799009900", 23)
pessoa2.imprimirCadastro()

#forma alternativa de passar os parametros da função
pessoa1.alterarCadastro(end="Rua Gen. Osorio, n589",
                        tel="6734312255",
                        idade=26)
pessoa1.imprimirCadastro()