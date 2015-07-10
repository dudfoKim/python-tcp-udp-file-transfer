import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffSize = 4096

host = socket.gethostname()
port = 1026

print(host)

s.bind(('', port))

s.listen(5)

while True:

  c, addr = s.accept()

  print "\nConectado com: " + str(addr) + "\n"

  f = open("duck_rec.jpg", "wb")

  l = c.recv(buffSize)

  while (l):
    f.write(l)
    print "Recebidos " + str(f.tell()) + " bytes..."
    l = c.recv(buffSize)

  print "\nRecebido!\n"

  f.close()
  c.close()

