import socket, json

# 30 pacotes
# 120406 bytes

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 16000000

host = socket.gethostname()
port = 1027

s.bind((host, port))

addr = (host, port)

f = open("duck_rec.jpg", "wb")

while True:

  tupla, addr = s.recvfrom(buffSize)

  tupla = unicode(tupla, 'latin-1')

  inpt = json.loads(tupla)

  index = inpt['index']
  data = inpt['data']

  if data == "done":
    f.close()
    s.close()
    break
  
  f.write(data.encode("utf-8"))

  print(index)