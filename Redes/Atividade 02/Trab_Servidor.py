from socket import*

def criandoServidor():
    portaServidor = 12000

    # ipv4 / TCP
    Servidor = socket(AF_INET,SOCK_STREAM)

    Servidor.bind(('',portaServidor))
    Servidor.listen(1) # numero de requisições

    print('Servidor pronto!')

    while 1:
        mensagem, endereco = Servidor.accept()
        recebeDecodificado = mensagem.recv(1024).decode()

        mensagemDec = recebeDecodificado.split('\n')
        auxiliar = str(mensagemDec[0])

        if(auxiliar.find("HelloWorld") != -1): # verificando se deve dar o retorno 200 ok
            retorno = "HTTP/1.1 200 OK \r\n"
            retorno += "Content-Type: text/html; charset=utf-8\r\n"
            retorno += "\r\n"
            retorno += "<html><body><p>Hello World<br><br>Welcome!</p></body></html>"

            mensagem.sendall(retorno.encode()) # retornando os dados
            mensagem.close()
            break

        elif(auxiliar.find("Hello_World") != -1): # verificando se deve dar o retorno 200 ok
            retorno = "HTTP/1.1 200 OK \r\n"
            retorno += "Content-Type: text/html; charset=utf-8\r\n"
            retorno += "\r\n"
            retorno += "<html><body><p>Hello World<br><br>Welcome!</p></body></html>"

            mensagem.sendall(retorno.encode()) # retornando os dados
            mensagem.close()
            break

        else:
            retorno = "HTTP/1.1 404 Not Found \r\n"
            retorno += "Content-Type: text/html; charset=utf-8\r\n"
            retorno += "\r\n"
            retorno += "<html><body><p>404 : Error<br><br>Página não encontrada!</p></body></html>"

            mensagem.sendall(retorno.encode()) # retornando os dados
            mensagem.close()
            break

criandoServidor()