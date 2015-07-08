import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1011

addr = (host, port)

fileName = "duck.jpg"

f = open(fileName, "rb")

data = f.read(buffSize)

s.sendto(fileName, addr)
s.sendto(data, addr)

while (data):
  if (s.sendto(data, addr)):
    print "Enviando..."
    data = f.read(buffSize)

print "Enviado!"

s.close()
f.close()
