import sqlite3 as conector
import sys

conexao = conector.connect("./GymDark.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

def linha(tam =  42):
    return '-' * tam

def Exibir_menu():
    print(linha())
    print("                  MENU")
    print(linha())
    print("1. Adicionar Aluno")
    print("2. Atualizar Aluno")
    print("3. Excluir Aluno")
    print("4. Exibir Cadastro de alunos")
    print("5. Buscar Aluno por Nome")
    print("6. Buscar Aluno por Telefone")
    print("7. Buscar Aluno por Email")
    print("8. Exibir Cadastro de Planos")
    print("9. Buscar Plano por Nome")
    print("10. Buscar Plano por Valor")
    print("11. Exibir cadastro de matriculas")
    print("12. Buscar matricula por aluno")
    print("13. Buscar matricula por plano")
    print("14. Buscar matricula por data de inicio")
    print("15. Atualizar plano")
    print("16. Atualizar matricula")
    print("17. Excluir plano")
    print("18. Excluir matricula")
    print("19. Sair")

#Logica para adicionar, Atualizar e Exluir alunos
def Adicionar_Alunos(conect,sql):
    try:
        cursor=conect.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Aluno adicionado!")
    except conector.DatabaseError as err:
        print(err)

def Atualizar_Alunos(conect,sql):
    try:
        cursor = conect.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Aluno atualizado!")
    except conector.DatabaseError as err:
        print(err)


def Atualizar_plano(conect,sql):
    try:
        cursor = conect.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Plano atualizado!")
    except conector.DatabaseError as err:
        print(err)


def Atualizar_Matricula(conect,sql):
    try:
        cursor = conect.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Matricula atualizada!")
    except conector.DatabaseError as err:
        print(err)


def Excluir_Alunos(conect,sql):
    try:
        cursor = conect.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Aluno excluido!")
    except conector.DatabaseError as err:
        print(err)

def Excluir_Plano(conect,sql):
    try:
        cursor = conect.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Plano excluido!")
    except conector.DatabaseError as err:
        print(err)

def Excluir_Matricula(conect,sql):
    try:
        cursor = conect.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Matricula excluido!")
    except conector.DatabaseError as err:
        print(err)


# Logica para exibir alunos, planos e matriculas existentes
def Exibir_alunos():
    print("Alunos existentes:")
    cursor.execute('SELECT * FROM Aluno')
    print(cursor.fetchall())

def Exibir_planos():
    print("Planos existentes:")
    cursor.execute('SELECT * FROM Plano')
    print(cursor.fetchall())

def Exibir_matriculas():
    print("Matriculas existentes:")
    cursor.execute('SELECT * FROM Matricula')
    print(cursor.fetchall())

#logica para buscas no banco de dados

def Buscar_Aluno_por_Nome(nome):
    cursor.execute("SELECT * FROM Aluno WHERE Nome LIKE ?", ('%' + nome + '%',))
    resultados = cursor.fetchall()
    if resultados:
        print("Alunos encontrados:")
        for aluno in resultados:
            print(aluno)
    else:
        print("Nenhum aluno encontrado com esse nome.")

def Buscar_Plano_por_Nome(nome):
    cursor.execute("SELECT * FROM Plano WHERE Nome LIKE ?",('%' + nome + '%',))
    resultados = cursor.fetchall()
    if resultados:
        print("Planos encontrados:")
        for plano in resultados:
            print(plano)
    else:
        print("Nenhum plano encontrado com esse nome.")


def Buscar_Plano_por_Valor(valor):
    cursor.execute("SELECT * FROM Plano WHERE Valor = ?", (valor,))
    resultados = cursor.fetchall()
    if resultados:
        print("Planos encontrados:")
        for plano in resultados:
            print(plano)
    else:
        print("Nenhum plano encontrado com esse valor.")



def Buscar_Aluno_por_Telefone(telefone):
    cursor.execute("SELECT * FROM Aluno WHERE Telefone = ?", (telefone,))
    resultados = cursor.fetchall()
    if resultados:
        print("Alunos encontrados:")
        for aluno in resultados:
            print(aluno)
    else:
        print("Nenhum aluno encontrado com esse telefone.")


def Buscar_Aluno_por_Email(email):
    cursor.execute("SELECT * FROM Aluno WHERE Email = ?", (email,))
    resultados = cursor.fetchall()
    if resultados:
        print("alunos encontrados:")
        for aluno in resultados:
            print(aluno)
    else:
        print("Nenhum aluno encontrado com esse Email.")


def Buscar_Matricula_por_aluno(aluno_id):
    cursor.execute("SELECT * FROM Matricula WHERE Aluno_Id = ?", (aluno_id,))
    resultados = cursor.fetchall()
    if resultados:
        print("matriculas encontradas:")
        for matricula in resultados:
            print(matricula)
    else:
        print("Nenhuma matricula encontrada para esse aluno.")


def Buscar_Matricula_por_plano(plano_id):
    cursor.execute("SELECT * FROM Matricula WHERE Plano_Id = ?",(plano_id,))
    resultados = cursor.fetchall()
    if resultados:
        print("matriculas encontradas:")
        for matricula in resultados:
            print(matricula)
    else:
        print("Nenhuma matricula encontrada para esse plano.")


def Buscar_Matricula_por_data_inicio(data_inicio):
    cursor.execute("SELECT * FROM Matricula WHERE Data_Inicio = ?", (data_inicio,))
    resultados = cursor.fetchall()
    if resultados:
        print("matriculas encontradas:")
        for matricula in resultados:
            print(matricula)
    else:
        print("Nenhuma matricula encontrada para essa data de inicio.")



def main():
    while True:
        Exibir_menu()
        opcao = input("Escolha uma opção:")
        if opcao == "1":
            nome = input("Digite o Nome:")
            data_nasc = input("Digite o Nascimento:")
            telefone = input("Digite o Telefone:")
            email = input("Digite o Email:")
            comando = "INSERT INTO Aluno ( Nome, Data_Nasc, Telefone , Email ) VALUES ('{}', '{}', '{}', '{}');".format(nome, data_nasc, telefone, email)
            Adicionar_Alunos(conexao, comando)
        elif opcao == "2":
            id = input("Digite seu ID:")
            nome = input("Digite o Nome:")
            data_nasc = input("Digite o Nascimento:")
            telefone = input("Digite o Telefone:")
            email = input("Digite o Email:")
            comando = "UPDATE Aluno SET Nome= '{}', Data_Nasc= '{}', Telefone= '{}', Email= '{}' WHERE Id= '{}';".format(nome, data_nasc, telefone, email, id)
            Atualizar_Alunos(conexao, comando)
        elif opcao == "3":
            id = input("Digite seu ID: ")
            comando = "DELETE FROM Aluno WHERE Id= '{}';".format(id)
            Excluir_Alunos(conexao, comando)
        elif opcao == "4":
            Exibir_alunos()
        elif opcao == "5":
            nome = input("Digite o nome do aluno:")
            Buscar_Aluno_por_Nome(nome)
        elif opcao == "6":
            telefone = input("Digite o telefone do aluno:")
            Buscar_Aluno_por_Telefone(telefone)
        elif opcao == "7":
            email = input("Digite o email do aluno:")
            Buscar_Aluno_por_Email(email)
        elif opcao == "8":
            Exibir_planos()
        elif opcao == "9":
            nome = input("Digite o nome do plano:")
            Buscar_Plano_por_Nome(nome)
        elif opcao == "10":
            valor = input("Digite o valor do plano:")
            Buscar_Plano_por_Valor(valor)
        elif opcao == "11":
            Exibir_matriculas()
        elif opcao == "12":
            id = input("Digite o id do aluno:")
            Buscar_Matricula_por_aluno(id)
        elif opcao == "13":
            id = input("Digite o id do plano:")
            Buscar_Matricula_por_plano(id)
        elif opcao == "14":
            data = input("Digite a data de inicio:")
            Buscar_Matricula_por_data_inicio(data)
        elif opcao == "15":
            id = input("Digite seu ID:")
            nome = input("Digite o Nome:")
            valor = input("Digite o Valor:")
            duracao = input("Digite a duração:")
            comando = "UPDATE Plano SET Nome= '{}', Valor= '{}', Duracao= '{}' WHERE Id= '{}';".format(nome, valor, duracao, id)
            Atualizar_plano(conexao, comando)
        elif opcao == "16":
            id = input("Digite seu ID:")
            data_inicio = input("Digite a data inicio:")
            data_fim = input("Digite a data fim:")
            aluno = input("Digite o id do aluno:")
            plano = input("Digite o id do plano:")
            comando = "UPDATE Matricula SET Data_Inicio= '{}', Data_fim= '{}', Aluno_Id= '{}', Plano_Id= '{}' WHERE Id= '{}';".format(data_inicio, data_fim, aluno, plano, id)
            Atualizar_Matricula(conexao, comando)
        elif opcao == "17":
            id = input("Digite seu ID:")
            comando = "DELETE FROM Plano WHERE Id= '{}';".format(id)
            Excluir_Plano(conexao, comando)
        elif opcao == "18":
            id = input("Digite seu ID:")
            comando = "DELETE FROM Matricula WHERE Id= '{}';".format(id)
            Excluir_Matricula(conexao, comando)

        elif opcao == "19":
            sys.exit()
        else:
            print("opção invalida. Tente novamente.")


if __name__ == "__main__":
    main()

# Fechamento das conexões
cursor.close()
conexao.close()