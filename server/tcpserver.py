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

  print "\nConnected with: " + str(addr) + "\n"

  f = open("file.mp4", "wb")

  l = c.recv(buffSize)

  while (l):
    f.write(l)
    print "Received " + str(f.tell()) + " bytes..."
    l = c.recv(buffSize)

  print "\nFile received!\n"

  f.close()
  c.close()
