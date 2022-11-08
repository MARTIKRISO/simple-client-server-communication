#==========================SERVER=========================

import socket, subprocess
from sys import exit
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
            conn.sendall("end".encode())
            print("Exiting")
            conn.close()
            exit()
        elif incomingTransmission == "hello":
            conn.sendall("hello".encode())
            print("Sent Hello World")
        elif incomingTransmission == "command":
            conn.sendall("command".encode())
            print("Initializing Command Communication")
            manageCommandTransmission(conn)
        sleep(1)

def manageCommandTransmission(conn):
    while 1:
        command = conn.recv(BUFFERSIZE).decode()
        if command == "end":
            print("Ending Command Communication")
            break
        else:
            resp = executeCommand()
            conn.sendall(resp.encode())


def executeCommand():
    #TODO: this

    return "commex"

handleConnection()
    #inp = input("Continue: (Y/n) ")
    #if inp.lower() == "n":
    #    exit(1)
    


