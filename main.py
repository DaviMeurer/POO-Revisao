from animal import animal
from veiculo import veiculo

#atribuindo dados
veiculo_modelo = input("Modelo do veiculo: ")
veiculo_roda = input("Quantas rodas possui o veículo: ")
veiculo_cor = input("Qual a cor do veículo: ")
veiculo_marca = input("Marca do veículo: ")

#objetos
carro1 = veiculo(veiculo_modelo, veiculo_roda, veiculo_cor, veiculo_marca)

carro1.registrarVeiculo()