from conexao import conectar

#DAO = Data Access Object: camada que faz a comunicação com o banco
class ClienteDAO:

    def inserir(self, cliente):

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO cliente(cpf, nome, telefone)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (
            cliente.cpf,
            cliente.nome,
            cliente.telefone
        ))

        conexao.commit()

    def listar(self):

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM cliente ORDER BY nome ASC")

        clientes = cursor.fetchall()
        return clientes

    def buscar_por_nome(self, nome):
        """Busca clientes por nome (busca parcial)"""
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM cliente WHERE nome LIKE %s",
            ('%' + nome + '%',)  # Busca parcial
        )

        clientes = cursor.fetchall()
        return clientes

    def buscar_por_cpf(self, cpf):
        """Busca cliente por CPF (exato)"""
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM cliente WHERE cpf = %s",
            (cpf,)
        )

        cliente = cursor.fetchone()
        return cliente

    def atualizar(self, cpf, nome, telefone1):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE cliente
            SET nome = %s,
                telefone1 = %s
            WHERE cpf = %s
        """, (nome, telefone1, cpf))

        conexao.commit()

    def excluir(self, cpf):

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM cliente WHERE cpf = %s",
            (cpf,)
        )

        conexao.commit()