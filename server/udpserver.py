import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1026

sckt.bind(("", port))

address = ("", port)

file = open("file.mp4", "wb")

data, address = sckt.recvfrom(buffSize)

while data:

    file.write(data)

    print("Receiving data...")

    if data == "done":
        file.close()
        sckt.close()
        break

    data, address = sckt.recvfrom(buffSize)
