import socket

s = socket.socket()

buffSize = 4096

host = socket.gethostname()
port = 1010

fileName = "duck.jpg"

s.connect((host, port))

f = open(fileName,"rb")

print "Host: " + host

l = f.read(buffSize)

while (l):
  s.send(l)
  print "Enviados " + str(f.tell()) + " bytes..."
  l = f.read(buffSize)

f.close()

print "Enviado!"
s.shutdown(socket.SHUT_WR)
print s.recv(buffSize)

s.close()
