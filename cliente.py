#Classe modelo que representa um cliente no sistema
class Cliente:

    def __init__(self, cpf=None, nome=None, email=None, rua=None, bairro=None, numero=None, telefone1=None, telefone2=None):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.telefone1 = telefone1
        self.telefone2 = telefone2
