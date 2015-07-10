import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1026

s.bind((host, port))

addr = (host, port)

f = open("labredes_rec.mp4", "wb")

data, addr = s.recvfrom(buffSize)

while (data):

  f.write(data)
  
  print "Recebendo dados..."

  if data == "done":
	f.close()
	s.close()
	break

  data, addr = s.recvfrom(buffSize)
