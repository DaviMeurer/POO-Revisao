class Produto:

    def __init__(self, parCod, parDescricao, parPreco, parQtd):
        self.cod=parCod
        self.descricao=parDescricao
        self.preco=parPreco
        self.qtd=parQtd

    def alteraPreco(self, novoPreco):
        self.preco=novoPreco