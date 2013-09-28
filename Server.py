__author__ = 'Chapo'

from socket import *


s = socket (AF_INET, SOCK_STREAM)
s.bind(('',8080))
s.listen(1)

while True:
    client,Ip = s.accept()
    print("Conexion hecha por %s " % str(Ip))
    client.send(("HTTP/1.1 200 OK"+"\x0D\x0A"+
                 "\x0D\x0A"+
                 "Respuesta=9").encode())

    client.close()

