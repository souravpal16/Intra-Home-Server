import socket
import sys
import select
from threading import *
import _thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv)!=3:
	print("correct usage: script, ip address, port number")
	exit()

ip_address = str(sys.argv[1])
port = int(sys.argv[2])

server.bind((ip_address, port))

server.listen(100)

list_of_clients = []

def clientThread(conn, addr):
    conn.send(b"Welcome to this chatroom!")
    #sends a message to the client whose user object is conn
    while True:
            try:     
                message = conn.recv(2048)    
                if message:
                    print("<" + addr[0] + "> " + message)
                    message_to_send = "<" + addr[0] + "> " + message
                    broadcast(message_to_send,conn)
                    #prints the message and address of the user who just sent the message on the server terminal
                else:
                    remove(conn)
            except:
                continue

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
	conn, addr = server.accept()
	list_of_clients.append(conn)
	print(addr[0] + ' connected')
	_thread.start_new_thread(clientThread, (conn, addr))

conn.close()
server.close()