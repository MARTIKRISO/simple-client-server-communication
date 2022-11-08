#==========================SERVER=========================

import socket, sys
from time import sleep
IP = "127.0.0.1"
PORT = 12345
MOTD = "Connection Established"
BUFFERSIZE = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))
sock.listen()

def handleConnection():
    conn, addr = sock.accept()
    manageConnection(conn, addr)
    
def manageConnection(conn, addr):
    print(f"Connected by {addr}")
    conn.sendall(MOTD.encode())
    print("Ready for communication")
    manageTransmission(conn)


def manageTransmission(conn: socket.socket):
    while 1:
        incomingTransmission = conn.recv(BUFFERSIZE).decode()
        print(f"Received: {incomingTransmission}")
            
        if incomingTransmission == "end":
            conn.sendall("Exiting".encode())
            print("Exiting")
            conn.close()
            sys.exit()
        elif incomingTransmission == "hello":
            conn.sendall("Hello World!".encode())
            print("Sent Hello World")
        
        
        sleep(1)

handleConnection()
    #inp = input("Continue: (Y/n) ")
    #if inp.lower() == "n":
    #    exit(1)
    


