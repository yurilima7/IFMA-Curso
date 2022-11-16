class Hotel:

    def __init__(self, Id_Hotel, Nome, Qtd_Quartos, Classe):
        self.Id_Hotel = Id_Hotel
        self.Nome = Nome
        self.Qtd_Quartos = Qtd_Quartos
        self.Classe = Classe

    def getID(self):
        return self.Id_Hotel

    def getNome(self):
        return self.Nome

    def getQuartos(self):
        return self.Qtd_Quartos

    def getClasse(self):
        return self.Classe