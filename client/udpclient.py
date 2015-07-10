import sys
import socket

# empty string: 37 bytes
# + 1 byte per character

counter = 1

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096 - 45

host = socket.gethostname()
port = 1027

addr = (host, port)

fileName = "duck.jpg"

f = open(fileName, "rb")

data = f.read(buffSize)
data = str(counter).zfill(8) + data

while True:

  data = f.read(buffSize)

  if not data:
    break

  data = str(counter).zfill(8) + data

  print "pack:" + data[:10]

  sckt.sendto(data, addr)
  counter += 1


if (sckt.sendto("done", addr)):
  print "Enviado!"

sckt.close()
f.close()
