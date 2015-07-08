import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffSize = 4096

host = socket.gethostname()
port = 1010

s.bind((host, port))

f = open("duck_rec.jpg", "wb")

s.listen(5)

while True:

  c, addr = s.accept()

  print "\nConectado com: " + str(addr) + "\n"

  l = c.recv(buffSize)

  while (l):
    f.write(l)
    print "Recebidos " + str(f.tell()) + " bytes..."
    l = c.recv(buffSize)

  print "\nRecebido!\n"

  f.close()
  c.close()

  break
