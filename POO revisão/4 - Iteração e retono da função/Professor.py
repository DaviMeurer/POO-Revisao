class Professor:
    def __init__(self, nome, materias):
        self.nome=nome
        self.disciplinas=materias


    def __str__(self) -> str: #retorna uma string
        return("Nome"+self.nome
                +" Disciplinas"+self.disciplinas)
        