from socket import *
from struct import *
import struct  
import sys
import _thread as thread
import time

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
        while (ascii_msg <= 96):
            ascii_msg += 26  
        out += chr(ascii_msg)
    return out

def client_connection(connection):

        
    # tamanho da string 
    string_size = int(struct.unpack("!i", connection.recv(4))[0])
    # recebe string do cliente
    string_byte = struct.unpack("!" + str(string_size) + "s", connection.recv(string_size))[0]
    
    # decodifica string
    string_received = string_byte.decode("ascii")
    
    # recebe a chave de decodificação
    key_cesar = int(struct.unpack("!i", connection.recv(4))[0])
    # decodifica string recebida
    string_decrypt = decrypt(string_received, key_cesar)
    
    # manda string decodificada
    connection.send(struct.pack("!" + str(string_size) + "s", string_decrypt.encode("ascii")))
    print(string_decrypt)
    connection.close()

def server():
    conn = socket(AF_INET, SOCK_STREAM)
    
    
    conn.bind((ip_address, port))

    conn.listen(5)

    while True:
        connection, address = conn.accept()
        connection.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        connection.setsockopt(SOL_SOCKET, SO_RCVTIMEO, struct.pack('ll', 15, 0))
        thread.start_new_thread(client_connection, (connection,)) 
server()


