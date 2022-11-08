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
        if received == "end": 
            print("Ending communication")
            sys.exit()
        elif received == "hello":
            print("Hello World!")
        elif received == "command":
            print("Initializing Command Communication")
            manageCommandTransmission()
    
def manageCommandTransmission():
    while 1:
        command = input("Enter command: ('exit' to end)")
        if command == "exit":
            sock.sendall("end".encode()) 
            print("Ending Command Communication")
            return  
        else:
            message = command.encode()
            sock.sendall(message)
        resp = sock.recv(BUFFERSIZE).decode()
        print(resp)
        
    

            


sleep(1)
manageTransmission()
