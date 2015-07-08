import socket

# 30 pacotes
# 120406 bytes

counter = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1011

s.bind((host, port))

addr = (host, port)

f = open("duck_rec.jpg", "wb")

data, addr = s.recvfrom(buffSize)

while (data):

  f.write(data)
  counter += 1
  print "count: " + str(counter)

  if counter == 30: # problem
    f.close()
    s.close()
    break

  data, addr = s.recvfrom(buffSize)
