from socket import *

import sys

# ip_address = sys.argv[1]
# port = int(sys.argv[2])
# string = sys.argv[3]
# key_cesar = int(sys.argv[4])

#
ip_address = 'localhost'
port = 5000
msg = [b'Ola mundo!']

conn = socket(AF_INET, SOCK_STREAM)
conn.connect((ip_address, port))

for linha in msg:
    conn.send(linha)
    data = conn.recv(1024)
    print('Client recived: ', data)

# """
# Encriptografar o texto
# """
# def encrypt(string, key_cesar):
#     out = ""
#     for char in string:
#         ascii_msg = ord(char) + key_cesar
#         if (ord(char) >= 122):
#             ascii_msg -= 26   
#         out += chr(ascii_msg)
#     return out

# print(encrypt(string, key_cesar))



