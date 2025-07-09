from ContaBancaria import ContaBancaria

minha_conta = ContaBancaria("Joao Dev", 100.00)

print(minha_conta.titular)
#print(minha_conta.__saldo) não funciona
#minha_conta.__alteraSaldo(120) não funciona

print(minha_conta.get_saldo())
minha_conta.set_saldo(-200)
print(minha_conta.get_saldo())