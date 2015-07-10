import socket

counter = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1026

addr = (host, port)

fileName = "duck.jpg"

f = open(fileName, "rb")

data = f.read(buffSize)

while (data):
  if (s.sendto(data, addr)):
    counter += 1
    print "Enviando..." + str(counter)
    data = f.read(buffSize)

print "Enviado!"

s.close()
f.close()
