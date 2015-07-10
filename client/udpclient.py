import sys
import socket, json

counter = 1

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1027

addr = (host, port)

fileName = "duck.jpg"

f = open(fileName, "rb")

data = f.read(buffSize)

conexao = json.dumps({'index' : 0, 'data' : data}, encoding="latin1")
sckt.sendto(conexao, addr)

while True:

  if not data:
    break

  msg, cliente = sckt.recvfrom(1027)

  print(msg)
  if msg == "ok" :
	  inpt = json.dumps({'index' : counter, 'data' : data}, encoding="latin1")

	  sckt.sendto(inpt, addr)
	  counter += 1

	  data = f.read(buffSize)
  else :
  	  inpt = json.dumps({'index' : counter, 'data' : data}, encoding="latin1")

	  sckt.sendto(inpt, addr)


if (sckt.sendto("done", addr)) :
	print "Enviado!"

sckt.close()
f.close()
