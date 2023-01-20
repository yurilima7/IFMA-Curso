import os

def main():
    os.system("clear")
    print('Digite 1 para a resolução de pagamento')
    op = int(input('Digite 2 para a resolução de organização\n'))
    os.system("clear")

    if(op == 1):
        pagamentos()
    elif(op == 2):
        levantamento()
    else:
        print("Opção inválida")
        main()


def pagamentos():
    segue = 1

    while(segue > 0):
        valor = float(input('Digite o valor do pagamento: '))

        if valor == 0: 
            segue = valor
            break

        dias = int(input('Digite quantidade de dias em atraso: '))
        
        segue = valorPagamento(valor, dias)

def valorPagamento(valor, diasAtraso):

    if diasAtraso > 0:

        calculaJuros = 0
        while(calculaJuros < diasAtraso):
            valor = valor * 1.1
            calculaJuros += 1

        valor = valor * 1.03

    print("Pagamento R$ {:.2f}\n".format(valor))

    return valor

def levantamento():
    controle, qtdMouse = True, 0
    qtdEsfera, qtdLimpeza, qtdTroca, qtdQuebradoInutilizado = 0, 0, 0, 0

    while(controle):
        print("Situacao do mouse\n")
        print("0 - Sair\n1 - Necessita da esfera\n2 - Necessita limpeza")
        print("3 - Necessita troca do cabo ou conector\n4 - Quebrado ou inutilizado\n")
        situacao = int(input())
        os.system("clear")

        if(situacao == 1):
            qtdEsfera += 1
            qtdMouse += 1

        elif(situacao == 2):
            qtdLimpeza += 1
            qtdMouse += 1

        elif(situacao == 3):
            qtdTroca += 1
            qtdMouse += 1

        elif(situacao == 4):
            qtdQuebradoInutilizado += 1
            qtdMouse += 1

        elif(situacao == 0):
            break

        else:
            print("Opcao invalida")

    print('Quantidade de mouses:', qtdMouse)
    print("\nSituação Quantidade Percentutal")
    print("1 - Necessita da esfera:", qtdEsfera, "| {:.2f}".format((100 * qtdEsfera) / qtdMouse),"%")
    print("2 - Necessita limpeza:", qtdLimpeza, "| {:.2f}".format((100 * qtdLimpeza) / qtdMouse),"%")
    print("3 - Necessita troca do cabo ou conector:", qtdTroca, "| {:.2f}".format((100 * qtdTroca) / qtdMouse),"%")
    print("4 - Quebrado ou inutilizado:", qtdQuebradoInutilizado, "| {:.2f}".format((100 * qtdQuebradoInutilizado) / qtdMouse),"%")

main()