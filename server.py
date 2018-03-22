from socket import *

import sys
import time

port = sys.argv[1]
#port = 5000
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
    size = connection.recv(1024) #recebe o tamanho da string??

    while True:    
        string = connection.recv(1024) #recebe a string
        if not string: break
        key_cesar = connecton.recv(1024) #recebe a chave para decriptografar
        string_out = decrypt(string, key_cesar) #decriptografar
        connection.send(b'Eco=>' + string_out)

connection.close()

"""
Decriptografar o texto
"""
def decrypt(string, key_cesar):
    out = ""
    for char in string:
        ascii_msg = ord(char) - key_cesar
        if (ord(char) >= 96):
            ascii_msg += 26   
        out += chr(ascii_msg)
    return out

print(encrypt(string, key_cesar))

