from socket import *

s = socket(AF_INET, SOCK_DGRAM)

buffSize = 1024

host = gethostname()
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
s.close()
f.close()
