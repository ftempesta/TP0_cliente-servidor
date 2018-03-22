from socket import *

import sys

ip_address = sys.argv[1]
port = int(sys.argv[2])
string = sys.argv[3]
key_cesar = int(sys.argv[4])

msg = [b'zzaa']

"""
Encriptografar o texto
"""
def encrypt(string, key_cesar):
    out = ""
    for char in string:
        ascii_msg = ord(char) + key_cesar
        if (ord(char) >= 122):
            ascii_msg -= 26   
        out += chr(ascii_msg)
    return out

print(encrypt(string, key_cesar))

"""
Conectar com servidor
"""
conn = socket(AF_INET, SOCK_STREAM)
conn.connect((ip_address, port))

"""
Enviar mensagem
"""
# TODO
# Após estabelecimento da conexão, 
# o cliente irá enviar um inteiro de quatro bytes
# em network byte order [send, htonl/pack] indicando o tamanho do string

for char in msg:
    conn.send(char) # como converto para bit???
    data = conn.recv(1024) # o que eu coloco aqui???
    #print('Client recived: ', data)

#TODO
"""
Enviar key_cesar
"""
conn.send(key_cesar)
key = conn.recv(1024)

#TODO
"""
Receber e imprimr resposta do servidor
"""

#TODO
"""
Fechar conexões
"""





