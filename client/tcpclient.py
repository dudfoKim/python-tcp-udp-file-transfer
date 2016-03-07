#coding: utf-8
import socket

buffSize = 4096

userinput = ""
hosts = []
port = 1026

while True:
  print("Type the address to send or 'ok' to begin the transmission:")
  userinput = raw_input()

  if userinput == "ok":
    break

  hosts.append(userinput)

fileName = "duck.jpg"

for h in hosts:

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((h, port))

  f = open(fileName, "rb")

  print "\nHost: " + h + "\n"

  data = f.read(buffSize)

  while (data):
    s.send(data)
    print "Sent " + str(f.tell()) + " bytes..."
    data = f.read(buffSize)

  print "\nSent to " + h + "\n"

  s.shutdown(socket.SHUT_WR)

  s.close()
  f.close()
