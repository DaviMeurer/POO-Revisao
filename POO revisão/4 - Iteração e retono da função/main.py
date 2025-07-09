from Professor import Professor


professor1 = Professor(nome="Rafael", materias=["Algoritmos", "Lógica", "POO"])
professor2 = Professor(nome="Erickson", materias=["Analise de Requisitos", "projeto Integrador"])
professores = [professor1,professor2] 

# print(professores)
# print(professores[0].nome)
# print(professores[0].disciplinas[1])
# print(professores[1].nome)

#iteração
# for objeto in professores:
#     print(objeto.nome)


#quero a posição de uma busca
# i = 0
# for objeto in professores:
#     if objeto.nome=="Erickson":
#         print("Posição ", i)
#         break
#     i+=1


#é mesma coisa que fazer isso=
for i, objeto in enumerate(professores):
    if objeto.nome=="Rafael":
        print("Posição ", i,objeto.nome )
        break

print(professor1.__str__())