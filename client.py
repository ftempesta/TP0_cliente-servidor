from socket import *
from struct import pack, unpack
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

#print(encrypt(string, key_cesar))

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
string_out = encrypt(string, key_cesar)
conn.send(pack("!i", len(string_out)))
conn.send(pack("!" + str(len(string_out)) + "s", string_out.encode("ascii")))


"""
Enviar key_cesar
"""
conn.send(pack("!i", key_cesar))


"""
Receber e imprimr resposta do servidor
"""
data_byte = unpack("!" + str(len(string_out)) + "s", conn.recv(len(string_out)))[0]
print(data_byte.decode("ascii"))


"""
Fechar conexões
"""
conn.close()





