#==========================CLIENT=========================

import socket, sys
from time import sleep
IP = "127.0.0.1"
PORT = 12345
BUFFERSIZE = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))


handshake = sock.recv(BUFFERSIZE)
print(f"{handshake.decode()}")

def manageTransmission():
    while 1:
        inp = input("Data to send: ")
        sock.send(inp.encode())
        received = sock.recv(BUFFERSIZE).decode()
        print(received)
        if inp == "end": sys.exit()

sleep(3)
manageTransmission()
