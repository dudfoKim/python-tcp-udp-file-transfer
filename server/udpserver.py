import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind(('localhost', 8081))

while True:
  data, addr = serversocket.recvfrom(1024)
  print ' > ' + data
