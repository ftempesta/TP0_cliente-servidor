from socket import *
from struct import *
import struct  
import sys
import time
import socketserver

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
Troca de dados com o cliente usando thread
"""
class client_streaming(socketserver.BaseRequestHandler):
    def handle(self):
        time.sleep(5)

        while True:    
           # tamanho da string 
           string_size = int(struct.unpack("!i", self.request.recv(4))[0])

           # recebe string do cliente
           string_byte = struct.unpack("!" + str(string_size) + "s", self.request.recv(string_size))[0]

           # decodifica string
           string_received = string_byte.decode("ascii")

           if not string_received: break
           # recebe a chave de decodificação
           key_cesar = int(struct.unpack("!i", self.request.recv(4))[0])

           # decodifica string recebida
           string_decrypt = decrypt(string_received, key_cesar)

           # manda string decodificada
           self.request.send(struct.pack("!" + str(string_size) + "s", string_decrypt.encode("ascii")))

        self.request.close()

"""
Criar servidor TCP/IP
"""
conn = socketserver.ThreadingTCPServer((ip_address, port), client_streaming)
conn.serve_forever()



   