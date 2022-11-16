from socket import*

serverName = 'localhost' # pega o endereço de IP local
serverPort = 12000 

# versão do ipv4 \ usando udp
cliente = socket(AF_INET,SOCK_DGRAM) 

mensagem = input('Digite uma mensagem: ')
opcao = input("Digite 1 para maiusculo ou 2 para minusculo: ")

#enviando mensagem para o servidor 
cliente.sendto(str.encode(mensagem),(serverName,serverPort))
cliente.sendto(str.encode(opcao),(serverName,serverPort)) 

novaMensagem, enderecoServidor = cliente.recvfrom(1024) # retorna a mensagem e o endereço de quem mandou a mesma
print(novaMensagem)