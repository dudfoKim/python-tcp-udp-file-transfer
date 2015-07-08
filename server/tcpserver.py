import socket

s = socket.socket()

buffSize = 4096

host = socket.gethostname()
port = 1010

s.bind((host, port))

f = open("duck_rec.jpg","wb")

s.listen(5)

while True:

  c, addr = s.accept()

  print "Conectado com: " + str(addr)

  l = c.recv(buffSize)

  while (l):
    f.write(l)
    print "Recebidos " + str(f.tell()) + " bytes..."
    l = c.recv(buffSize)

  f.close()

  print "Recebeu!"

  c.close()
