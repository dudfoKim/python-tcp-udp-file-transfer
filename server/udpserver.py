import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1011

s.bind((host, port))

addr = (host, port)

f = open("duck_rec.jpg", "wb")

data,addr = s.recvfrom(buffSize)
try:
  while (data):
    f.write(data)
    s.settimeout(10)
    data, addr = s.recvfrom(buffSize)
except socket.timeout:
  f.close()
  s.close()
  print "Recebido!"
