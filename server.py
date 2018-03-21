from socket import *

import sys
import time

# port = sys.argv[1]
port = 5000
ip_address = ''

"""
Criar servidor TCP/IP
AF_INET = protocolo de endereço ip
SOCK_STREAM = protocolo de transferência TCP
"""
conn = socket(AF_INET, SOCK_STREAM)

"""
Vínculo entre servidor e port
"""
conn.bind((ip_address, port))

"""
Quantidade de clientes
"""
conn.listen(5)

while True:
    connection, address = conn.accept()
    print('Server connect by ', address)

    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send(b'Eco=>' + data)

connection.close()