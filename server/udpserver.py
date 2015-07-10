import socket, json

# 30 pacotes
# 120406 bytes

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 16000000
counter = 1

host = socket.gethostname()
port = 1027

s.bind(('', port))

addr = (host, port)

f = open("duck_rec.jpg", "wb")

while True:
  
  tupla, addr = s.recvfrom(buffSize)

  if tupla == "done" :
    f.close()
    s.close()
    break

  tupla = unicode(tupla, 'latin-1')

  inpt = json.loads(tupla)

  index = inpt['index']
  data = inpt['data']
  
  print (data[0:10])

  if index == 0 :
  	s.sendto("ok", addr)
  	continue

  if index == counter :
  	s.sendto("ok", addr)
  	f.write(data.encode("utf-8"))
  	counter = counter + 1
  	print(index)
  else:
  	s.sendto(str(counter), addr)
