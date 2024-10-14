import sqlite3 as conector
from Class import Aluno, Plano, Matricula

conexao = conector.connect("./GymDark.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()


# Inserção de dados na tabela Aluno
comando1 = '''INSERT INTO Aluno
                VALUES (:Id, :Nome, :Data_Nasc, :Telefone, :Email);'''

aluno1 = Aluno(1, "joão Silva", "1980-01-01", "(31)9999-9999", "joaosilva@email.com")
aluno2 = Aluno(2, "Maria Oliveira", "1990-02-02", "(31)8888-8888", "mariaoliveira@email.com")
aluno3 = Aluno(3, "Pedro Souza", "2000-03-03", "(31)7777-7777", "pedrosouza@email.com")
cursor.execute(comando1, vars(aluno1))
cursor.execute(comando1, vars(aluno2))
cursor.execute(comando1, vars(aluno3))


# Inserção de dados na tabela Plano
comando2 = '''INSERT INTO Plano
                VALUES (:Id, :Nome, :Valor, :Duracao);'''
plano1 = Plano(1, "Basico", 100, 1)
plano2 = Plano(2, "Intermediario", 150, 3)
plano3 = Plano(3, "Avançado", 200, 6)
cursor.execute(comando2, vars(plano1))
cursor.execute(comando2, vars(plano2))
cursor.execute(comando2, vars(plano3))


# Inserção de dados na tabela Plano
comando3 = '''INSERT INTO Matricula
                VALUES (:Id, :Data_inicio, :Data_fim, :Aluno_Id, :Plano_Id);'''
matricula1 = Matricula(1, "2024-04-01", "2024-05-01", 1,1 )
matricula2 = Matricula(2, "2024-03-01", "2024-06-01", 2, 2)
cursor.execute(comando3, vars(matricula1))
cursor.execute(comando3, vars(matricula2))


# Efetivação do comando
conexao.commit()
# Fechamento das conexões
cursor.close()
conexao.close()