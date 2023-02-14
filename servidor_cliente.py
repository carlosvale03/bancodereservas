import socket 

def servidor_cliente(ip, port):
    '''
    Cria um socket e se conecta a um servidor remoto em um determinado endereço IP e porta.

    Parameters:
        ip (str): O endereço IP do servidor remoto.
        port (int): A porta do servidor remoto.

    Returns:
        Um objeto socket conectado ao servidor remoto.
    '''
    addr = (ip, port) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(addr)
    return client_socket