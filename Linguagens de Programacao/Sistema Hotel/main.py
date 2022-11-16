from modelo.Hotel import Hotel
from modelo.Hospede import Hospede
from modelo.Operacoes import Operacoes

def cadastrarHotel():
    nome = input("Digite o nome do hotel: ")
    quartos = int(input("Digite a quantidade de Quartos "))
    classe = input("Quarto de classe? ")
    id = int(input("Digite o id do Hotel: "))

    hotel = Hotel(Id_Hotel = id, Nome = nome, Qtd_Quartos = quartos, Classe = classe)
    
    op = Operacoes()
    op.cadastrarHotel(hotel)

def cadastrarHospede():
    nome = input("Digite o nome do Hospede: ")
    cpf = input("Digite o CPF: ")
    dias = int(input("Digite a quantidade de dias ficará hospedado: "))
    num = int(input("Informe o número do quarto: "))
    idH = int(input("Digite o id do Hotel: "))
    idHospede = int(input("Digite o id do Hospede: "))

    hospede = Hospede(Id_Hospede = idHospede, Nome = nome, CPF = cpf, Qtd_Dias = dias, Num_Quarto = num, Id_Hotel_id = idH)

    op = Operacoes()
    op.cadastrarHospede(hospede)

def listaHospedes():
    op = Operacoes()
    resultado = op.listarHospedes()
    print(resultado)

def buscarHospedes():
    id = int(input("Digite o id do hospede buscado: "))
    op = Operacoes()
    resultado = op.buscarHospede(id)
    print("Dados da busca")
    print(resultado)

def deletarHospede():
    id = int(input("Digite o id do Hospede para excluir: "))
    op = Operacoes()
    op.deletarHospede(id)

def deletarHotel():
    id = int(input("Digite o id do Hotel para excluir: "))
    op = Operacoes()
    op.deletarTabHospedes()
    op.deletarHotel(id)

def main():

    sair = False

    while(sair == False):

        print("\tDigite\n| 1 - Cadastrar Hospede\n| 2 - Buscar todos os Hospedes\n| 3 - Buscar um Hospede\n| 4 - Deletar Hospede\n| 5 - Deletar Hotel \n| 6 - Cadastrar Hotel\n| 0 - Sair")
        opcao = int(input())

        if(opcao == 1):
            cadastrarHospede()
        elif(opcao == 2):
            listaHospedes()
        elif(opcao == 3):
            buscarHospedes()
        elif(opcao == 4):
            deletarHospede()
        elif(opcao == 5):
            deletarHotel()
        elif(opcao == 6):
            cadastrarHotel()
        elif(opcao == 0):
            sair = True
        else:
            print("opcao inválida!")


main()