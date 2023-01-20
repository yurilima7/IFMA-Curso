from socket import*

serverPort = 12000

# versão do ipv4 \ usando udp
servidor = socket(AF_INET, SOCK_DGRAM)

servidor.bind(('',serverPort))
print('O servidor está funcionando!')

while 1:
    mensagem, enderecoCliente = servidor.recvfrom(1024)
    opcao, cA2 = servidor.recvfrom(1024)
    escolha = int(opcao)
    if escolha == 1:
        novaMensagem = mensagem.upper()
        servidor.sendto(novaMensagem, enderecoCliente)
    elif escolha == 2:
        novaMensagem = mensagem.lower()
        servidor.sendto(novaMensagem, enderecoCliente)
