import socket

buffSize = 4096

user_input = ""
hosts = []
port = 1026

while True:
    print("Type the address to send or 'ok' to begin the transmission:")
    user_input = raw_input()

    if user_input == "ok":
        break

    hosts.append(user_input)

fileName = "duck.jpg"

for host in hosts:

    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.connect((host, port))

    file = open(fileName, "rb")

    print("\nHost: " + host + "\n")

    data = file.read(buffSize)

    while data:
        sckt.send(data)
        print("Sent " + str(file.tell()) + " bytes...")
        data = file.read(buffSize)

    print("\nSent to " + host + "\n")

    sckt.shutdown(socket.SHUT_WR)

    sckt.close()
    file.close()
