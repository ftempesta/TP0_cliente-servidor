from socket import *
from struct import *
import struct  
import sys


"""
Ler parâmetros
"""
port = int(sys.argv[1])
ip_address = ''

"""
Decriptografar o texto
"""
def decrypt(string, key_cesar):
    out = ""
    for char in string:
        ascii_msg = ord(char) - key_cesar
        if (ascii_msg <= 96):
            ascii_msg += 26  
        out += chr(ascii_msg)
    return out

"""
Criar servidor TCP/IP
AF_INET = protocolo de endereço ip
SOCK_STREAM = protocolo de transferência TCP
"""
conn = socket(AF_INET, SOCK_STREAM)
conn.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
conn.setsockopt(SOL_SOCKET, SO_RCVTIMEO, struct.pack('ll', 15, 0))

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
    
    # tamanho da string 
    string_size = int(struct.unpack("!i", connection.recv(4))[0])

    # recebe string do cliente
    string_byte = struct.unpack("!" + str(string_size) + "s", connection.recv(string_size))[0]
    
    # decodifica string
    string_received = string_byte.decode("ascii")
    
    if not string_received: break
    # recebe a chave de decodificação
    key_cesar = int(struct.unpack("!i", connection.recv(4))[0])
    # decodifica string recebida
    string_decrypt = decrypt(string_received, key_cesar)
    
    # manda string decodificada
    connection.send(struct.pack("!" + str(string_size) + "s", string_decrypt.encode("ascii")))

"""
Fechar conexão
"""

connection.close()