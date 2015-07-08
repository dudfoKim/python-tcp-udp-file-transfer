from socket import *

s = socket(AF_INET, SOCK_DGRAM)

buffSize = 1024

host = gethostname()
port = 1011

s.bind((host, port))

addr = (host, port)

f = open("duck_rec.jpg", "wb")

data,addr = s.recvfrom(buffSize)
try:
  while (data):
    f.write(data)
    s.settimeout(2)
    data, addr = s.recvfrom(buffSize)
except timeout:
  f.close()
  s.close()
  print "Recebido!"
