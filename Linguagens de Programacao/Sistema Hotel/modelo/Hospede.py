class Hospede:

    def __init__(self, Id_Hospede, Nome, CPF, Qtd_Dias, Num_Quarto, Id_Hotel_id):
        self.Id_Hospede = Id_Hospede
        self.Nome = Nome
        self.CPF = CPF
        self.Qtd_Dias = Qtd_Dias
        self.Num_Quarto = Num_Quarto
        self.Id_Hotel_id = Id_Hotel_id

    def getID(self):
        return self.Id_Hospede

    def getNome(self):
        return self.Nome

    def getCPF(self):
        return self.CPF

    def getDias(self):
        return self.Qtd_Dias

    def getQuarto(self):
        return self.Num_Quarto

    def getEstrangeira(self):
        return self.Id_Hotel_id