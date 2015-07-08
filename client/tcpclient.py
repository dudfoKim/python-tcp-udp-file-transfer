import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffSize = 4096

host = socket.gethostname()
port = 1010

fileName = "duck.jpg"

s.connect((host, port))

f = open(fileName, "rb")

print "\nHost: " + host + "\n"

l = f.read(buffSize)

while (l):
  s.send(l)
  print "Enviados " + str(f.tell()) + " bytes..."
  l = f.read(buffSize)

print "\nEnviado!\n"

s.shutdown(socket.SHUT_WR)

s.close()
f.close()
