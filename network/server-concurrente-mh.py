#!/usr/bin/python
import socket
import threading

def cliente(newdesc):
    leido = newdesc.recv(2048)
    while ( leido[0:4] != "exit"):
        print leido
        newdesc.send(leido.upper()[::-1])
        newdesc.send("\n")
        leido = newdesc.recv(2048)
    newdesc.close()

desc= socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
# para que no diga address already in use ...
desc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#servidor=raw_input("mi ip:")
#port=raw_input("mi port:")
desc.bind(("192.168.14.250", 5000))
desc.listen(20)
while True:
    newdesc,cli = desc.accept()
    print cli
    t1 = threading.Thread(target=cliente, args=(newdesc,))
    t1.start()
#    t1.join()  ...serializa 

