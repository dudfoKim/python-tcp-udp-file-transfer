import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffSize = 4096

host = socket.gethostname()
port = 1026

print(host)

sckt.bind(('', port))

sckt.listen(5)

while True:

    c, address = sckt.accept()

    print("\nConnected with: " + str(address) + "\n")

    file = open("file.mp4", "wb")

    l = c.recv(buffSize)

    while l:
        file.write(l)
        print("Received " + str(file.tell()) + " bytes...")
        l = c.recv(buffSize)

    print("\nFile received!\n")

    file.close()
    c.close()
