#Classe modelo que representa um funcionário
class Funcionario:

    def __init__(self, id_funcionario=None, cpf=None, nome=None, funcao=None):
        self.id_funcionario = id_funcionario
        self.cpf = cpf
        self.nome = nome
        self.funcao = funcao

