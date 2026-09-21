from conexao import conectar
from funcionario import Funcionario

#DAO = Data Access Object: camada que faz a comunicação com o banco
class FuncionarioDAO:

    def inserir(self, funcionario):

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO funcionario(cpf,nome,funcao)
        VALUES(%s,%s,%s)
        """

        cursor.execute(sql,
                       (funcionario.cpf,
                        funcionario.nome,
                        funcionario.funcao))

        conexao.commit()

    def listar(self):

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM funcionario")

        dados = cursor.fetchall()

        return dados

    def buscar_por_nome(self, nome):
        """Busca funcionários por nome (busca parcial)"""
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM funcionario WHERE nome LIKE %s"
        cursor.execute(sql, ('%' + nome + '%',))

        resultados = cursor.fetchall() #fetchall() retorna uma lista de tuplas
        funcionarios = []

        for linha in resultados:
            #Para cada linha cria um objeto funcionario
            funcionario = Funcionario(
                id_funcionario=linha[0],
                cpf=linha[1],
                nome=linha[2],
                funcao=linha[3]
            )
            funcionarios.append(funcionario)

        return funcionarios

    def buscar_por_cpf(self, cpf):
        """Busca funcionário por CPF (exato)"""
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM funcionario WHERE cpf = %s",
            (cpf,)
        )

        resultado = cursor.fetchone()

        if resultado:
            return Funcionario(
                id_funcionario=resultado[0],
                cpf=resultado[1],
                nome=resultado[2],
                funcao=resultado[3]
            )
        return None

    def atualizar(self, cpf, novo_nome, nova_funcao):

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE funcionario
            SET nome=%s,
                funcao=%s
            WHERE cpf=%s
        """, (novo_nome, nova_funcao, cpf))

        conexao.commit()

    def excluir(self, cpf):

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM funcionario WHERE cpf=%s",
            (cpf,)
        )

        conexao.commit()