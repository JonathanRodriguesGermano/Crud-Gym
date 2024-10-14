import sqlite3 as conector

conexao = conector.connect("./GymDark.db")
cursor = conexao.cursor()

comando = '''CREATE TABLE Plano (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nome TEXT NOT NULL, 
                        Valor FLOAT NOT NULL,
                        Duracao INTEGER NOT NULL
                        );'''
cursor.execute(comando)
# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()