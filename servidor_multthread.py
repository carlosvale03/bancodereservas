import threading
import socket
from banco_mysql import Banco


class ClientThread(threading.Thread):
    """
    Esta classe representa uma thread para lidar com um cliente conectado ao servidor.
    """
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket

    def run(self):
        """
        Método executado quando a thread é iniciada.
        Recebe os dados enviados pelo cliente, identifica o método a ser executado e chama a função correspondente
        na classe Banco. Depois, envia a resposta de volta para o cliente.
        """
        recebe = ''
        while True:
            # define o tamanho dos pacotes recebidos
            data = self.csocket.recv(2048)
            recebe = data.decode().split("*")
            if recebe == ['']:
                break
            metodo = recebe.pop(0)
            if metodo != "verificaSenha":
                print(f"Metodo {metodo} chamado da conta {recebe[0]}\n")
            banco = Banco()
            func = getattr(banco, metodo)
            re = func(*recebe)
            self.csocket.send(f'{re}'.encode('utf-8'))  # 'utf-8'
        print("Client at ", clientAddress, "disconected...")


if __name__ == "__main__":
    host = 'localhost'
    port = 8000
    addr = (host, port)
    server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)  # cria um socket
    # define a porta e quais ips podem se conectar no servidor
    server.bind(addr)
    print("servidor iniciado!")
    print("aguardando nova conexao...")

    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        print(f"clientsock: {clientsock} \nclientAddress: {clientAddress}")
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
