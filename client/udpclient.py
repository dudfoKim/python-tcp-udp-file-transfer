import socket

counter = 0

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1026

address = (host, port)

fileName = "file.mp4"

file = open(fileName, "rb")

while True:

    print("Sending data...")

    data = file.read(buffSize)

    if not data:
        break

    sckt.sendto(data, address)


if sckt.sendto("done", address):
    print("Sent!")

sckt.close()
file.close()
