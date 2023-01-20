from banco.Banco import Banco

class Operacoes:

    def __init__ (self):
        pass

    def deletarHospede(self, id):
        bd = Banco().conectar()
        delete = bd.cursor()
        delete.execute("delete from Hospede where Id_Hospede = " + str(id))
        bd.commit()
        print("Hospede removido!")
        

    def deletarHotel(self, id):
        bd = Banco().conectar()
        delete = bd.cursor()
        delete.execute("delete from Hotel where Id_Hotel = " + str(id))
        bd.commit()
        print("Hotel removido!")

    def listarHospedes(self):
        bd = Banco().conectar()
        lista = bd.cursor()
        lista.execute("select * from Hospede" )
        return lista.fetchall()

    def buscarHospede(self, id):
        bd = Banco().conectar()
        busca = bd.cursor()
        busca.execute("select * from Hospede where Id_Hospede = " + str(id) )
        return busca.fetchall()

    def cadastrarHotel(self, hotel):
        bd  = Banco().conectar()
        cad = bd.cursor()
        script = "insert into Hotel (Id_Hotel, Nome, Qtd_Quartos, Classe ) values ('"+str(hotel.getID())+"', '"+hotel.getNome()+"', '"+str(hotel.getQuartos())+"', '"+hotel.getClasse()+"')"
        cad.execute(script)
        bd.commit()      
        print("Hotel cadastrado com sucesso!")

    def cadastrarHospede(self, hospede):
        bd  = Banco().conectar()
        cad = bd.cursor()
        script = "insert into Hospede (Id_Hospede, Nome,  CPF,  Qtd_Dias,  Num_Quarto, Id_Hotel_id) values ('"+str(hospede.getID())+"', '"+str(hospede.getNome())+"', '"+str(hospede.getCPF())+"', '"+str(hospede.getDias())+"', '"+str(hospede.getQuarto())+"', '"+str(hospede.getEstrangeira())+"')"
        cad.execute(script)
        bd.commit()
        print("Hospede cadastrado com sucesso!")
    
    def deletarTabHospedes(self):
        bd = Banco().conectar()
        delete = bd.cursor()
        script = "delete from Hospede"
        delete.execute(script)
        bd.commit()
        print("Todos os clientes foram deletados")


    