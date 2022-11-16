import psycopg2

class Banco:

    def __init__(self):
        self.bd = None

    def conectar(self):
        self.bd = psycopg2.connect(host = "localhost", database="Hotel",
                                    user="postgres", password="Ghost@20")

        print("Conexao Realizada com sucesso!")
        return self.bd

    def desconectar(self):
        self.bd.close()
