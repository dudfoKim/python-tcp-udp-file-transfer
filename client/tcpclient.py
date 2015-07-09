#coding: utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffSize = 4096

userinput = ""
hosts = []

while True:
	print("Digite um endereço para envio, ou ok para iniciar a transmissão")
	userinput = raw_input()

	if userinput == "ok":
		break

	hosts.append(userinput)

port = 1026

fileName = "duck.jpg"

for h in hosts:
	s.connect((h, port))

	f = open(fileName, "rb")

	print "\nHost: " + h + "\n"

	data = f.read(buffSize)

	while (data):
	  s.send(data)
	  print "Enviados " + str(f.tell()) + " bytes..."
	  data = f.read(buffSize)

	print "\nEnviado para " + h + "\n"

	s.shutdown(socket.SHUT_WR)

	s.close()
	f.close()
