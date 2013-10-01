__author__ = 'Chapo'

from socket import *


s = socket (AF_INET, SOCK_STREAM)
s.bind(('',8080))
s.listen(1)
comd = 0

while True:
    client,Ip = s.accept()
    print("Conexion hecha por %s " % str(Ip))
    client.send(("HTTP/1.1 200 OK"+"\x0D\x0A"+
                 "\x0D\x0A"+
                 "Respuesta=9").encode())
    #if comd == 0:
    #    client.send(("HTTP/1.1 200 OK"+"\x0D\x0A"+
    #             "\x0D\x0A"+
    #             "Respuesta=50x01,0x06,0x00,0x02,0x00,0x80").encode())
    #    comd = 1
    #else:
    #    client.send(("HTTP/1.1 200 OK"+"\x0D\x0A"+
    #             "\x0D\x0A"+
    #             "Respuesta=50x01,0x06,0x00,0x02,0x00,0x00").encode())
    #    comd = 0


    client.close()

