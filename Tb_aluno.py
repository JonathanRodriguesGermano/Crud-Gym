import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./GymDark.db")
    cursor = conexao.cursor()

    # Execução de um comando: SELECT... CREATE ...
    comando = '''CREATE TABLE Aluno (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT NOT NULL,
                    Data_Nasc DATE NOT NULL,
                    Telefone TEXT NOT NULL,
                    Email TEXT NOT NULL
                    );'''
    cursor.execute(comando)
    # Efetivação do comando
    conexao.commit()
except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
