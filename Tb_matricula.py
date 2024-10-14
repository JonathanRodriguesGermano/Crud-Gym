import sqlite3 as conector

conexao = conector.connect("./GymDark.db")
cursor = conexao.cursor()

comando = '''CREATE TABLE Matricula (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Data_Inicio DATE NOT NULL,
                        Data_fim DATE NOT NULL,
                        Aluno_Id INTEGER NOT NULL,
                        Plano_Id INTEGER NOT NULL,                         
                        FOREIGN KEY(Aluno_Id) REFERENCES Aluno(Id),
                        FOREIGN KEY(Plano_Id) REFERENCES Plano(Id)                     
                        );'''
cursor.execute(comando)
# Efetivação do comando
conexao.commit()
# Fechamento das conexões
cursor.close()
conexao.close()
