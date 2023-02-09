import socket
from banco_mysql import Banco

host = "localhost"
port = 8006
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket
serv_socket.bind(addr) # define a porta e quais ips podem se conectar no servidor
serv_socket.listen(10) # define o limite de conexoes
print('Agrardando conexão...')
con, cliente = serv_socket.accept() #servidor aguardando conexao
print('Conectado!')
print('Aguardando mensagem...')

while True:
    try:
        # define o tamanho dos pacotes recebidos
        recebe = con.recv(2048).decode().split("*")
        print(f"recebe completo: {recebe}")
        metodo = recebe.pop(0)
        print(f"O metodo é {metodo}")
        print(f"recebe sem o metodo: {recebe}")
        if recebe == []:
            serv_socket.close()
            break
        banco = Banco()
        func = getattr(banco, metodo)
        re = func(*recebe)
        print(f"re {re}")
        con.send(f'{re}'.encode('utf-8'))  # 'utf-8'
    except:
        serv_socket.close()
