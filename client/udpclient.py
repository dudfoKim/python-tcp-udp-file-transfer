import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = 'hello UDP'
addr = ('localhost', 8081)
clientsocket.sendto(data, addr)
