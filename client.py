from socket import *
from struct import *
import struct
import sys


"""
Ler parâmetros
"""
ip_address = sys.argv[1]
port = int(sys.argv[2])
string = sys.argv[3]
key_cesar = int(sys.argv[4])

"""
Encriptografar o texto
"""
def encrypt(string, key_cesar):
    out = ""
    for char in string:
        ascii_msg = ord(char) + key_cesar
        while (ascii_msg > 122):
            ascii_msg -= 26   
        out += chr(ascii_msg)
    return out

"""
Conectar com servidor e Enviar mensagem
"""
conn = socket(AF_INET, SOCK_STREAM)
conn.connect((ip_address, port))
conn.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# criptografar mensagem
string_encrypt = encrypt(string, key_cesar).encode("ascii")

# envio de um inteiro de quatro bytes indicando o tamanho do string
conn.send(struct.pack("!i", len(string_encrypt)))

# envio da mensagm criptografada
conn.send(struct.pack("!" + str(len(string_encrypt)) + "s", string_encrypt))

# envio da chave para decriptografar
conn.send(struct.pack("!i", key_cesar))

"""
Receber e imprimr resposta do servidor
"""
string_back = conn.recv(len(string_encrypt)) 

data_byte = struct.unpack("!" + str(len(string_encrypt)) + "s", string_back)[0]

print(data_byte.decode("ascii"))

"""
Fechar conexão
"""
conn.close()