import socket 
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv)!=3:
	print('correct usage: script, ip address, port number')
	exit()

ip_address = '192.168.29.37'
port = 65432
server.connect((ip_address, port))

while True:
	socket_list = [sys.stdin, server]
	read_sockets, write_socket, error_socket = select.select(socket_list, [], [])

	for socks in read_sockets:
		if socks == server:
			message = socks.recv(2048)
			print(message)

		else:
			message = sys.stdin.readline()
			text = message.encode('utf-8')
			server.send(text)
			sys.stdout.write('<You>')
			sys.stdout.write(message)
			sys.stdout.flush()
server.close()