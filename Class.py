class Aluno:
    def __init__(self, Id, Nome, Data_Nasc, Telefone, Email ):
        self.Id = Id
        self.Nome = Nome
        self.Data_Nasc = Data_Nasc
        self.Telefone = Telefone
        self.Email = Email

class Plano:
    def __init__(self, Id, Nome, Valor, Duracao):
        self.Id = Id
        self.Nome = Nome
        self.Valor = Valor
        self.Duracao = Duracao

class Matricula:
    def __init__(self, Id,  Data_inicio, Data_fim, Aluno_Id, Plano_Id ):
        self.Id = Id
        self.Data_inicio = Data_inicio
        self.Data_fim = Data_fim
        self.Aluno_Id = Aluno_Id
        self.Plano_Id = Plano_Id
