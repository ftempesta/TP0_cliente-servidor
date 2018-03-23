from socket import *
import struct  
import sys
import time

port = int(sys.argv[1])
ip_address = ''

"""
Decriptografar o texto
"""
def decrypt(string, key_cesar):
    out = ""
    for char in string:
        ascii_msg = ord(char) - key_cesar
        if (ord(char) < 97):
            ascii_msg += 26   
        out += chr(ascii_msg)
    return out

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
    size = int(struct.unpack("!i", connection.recv(4))[0])

    while True:    
        data_byte = struct.unpack("!" + str(size) + "s",connection.recv(size))[0]
        string = data_byte.decode("ascii")
        
        if not string: break
        key_cesar = int(struct.unpack("!i", connection.recv(4))[0])
        print(size, string, key_cesar)

        string_out = decrypt(string, key_cesar) #decriptografar
        print(string_out)
        conn.send(struct.pack("!" + str(size) + "s", string_out.encode("ascii")))

connection.close()



