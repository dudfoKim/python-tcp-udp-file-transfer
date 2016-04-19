import socket

buffSize = 4096

fileName = "duck.jpg"

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 1026

address = (host, port)

file = open(fileName, "rb")

print("\nHost: " + host + "\n")

data = file.read(buffSize)

while data:

    sckt.sendto(data, address)
    print("Sent " + str(file.tell()) + " bytes...")
    data = file.read(buffSize)


if sckt.sendto(b"done", address):
    print("\nFile sent to " + host + "\n")

sckt.close()
file.close()
