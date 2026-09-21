import mysql.connector

conexao = None

def conectar():
    global conexao #Variavel global usada para armazenar o objeto de conexão com o banco

    #Se já existe uma conexão aberta, reutiliza
    if conexao is not None and conexao.is_connected():
        return conexao

    while True:
        senha = input("Digite a senha do MySQL: ")

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password=senha,
                database="locadora_bd"
            )

            print("\nConectado com sucesso!\n")
            return conexao

        except mysql.connector.Error:
            print("\nSenha incorreta. Tente novamente.\n")