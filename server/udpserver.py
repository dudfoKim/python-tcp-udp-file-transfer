import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buffSize = 4096

host = socket.gethostname()
port = 1026

print("Host: " + host)

sckt.bind(("", port))

address = ("", port)

file = open("duck.jpg", "wb")

data, address = sckt.recvfrom(buffSize)

print("\nConnected with: " + str(address) + "\n")

while data:

    file.write(data)

    print("Received " + str(file.tell()) + " bytes...")

    if data == b"done":
        print("\nFile received!\n")
        file.close()
        sckt.close()
        break

    data, address = sckt.recvfrom(buffSize)
