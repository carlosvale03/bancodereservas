import socket 

def servidor_cliente(ip, port):
    # ip = "localhost"             # '192.168.186.160' 
    # port = port
    addr = (ip, port) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(addr)
    return client_socket