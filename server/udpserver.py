import socket

# 30 pacotes
# 120406 bytes

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1027

print(host)
s.bind((host, port))

addr = (host, port)

f = open("duck_rec.jpg", "wb")

data, addr = s.recvfrom(buffSize)

while (data):

  print "pack:" + data[:10]

  if data == "done":
    f.close()
    s.close()
    break

  f.write(data)

  data, addr = s.recvfrom(buffSize)
