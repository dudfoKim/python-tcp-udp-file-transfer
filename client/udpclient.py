import socket

counter = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1026

addr = (host, port)

fileName = "file.mp4"

f = open(fileName, "rb")

while True:

  print "Sending data..."

  data = f.read(buffSize)

  if not data:
    break

  s.sendto(data, addr)


if (s.sendto("done", addr)):
  print "Sent!"

s.close()
f.close()
