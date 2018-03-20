import sys
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
        if (ord(char) >= 122):
            ascii_msg -= 26   
        out += chr(ascii_msg)
    return out

print(encrypt(string, key_cesar))

