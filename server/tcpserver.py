import socket

buffSize = 4096

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 1026

print("Host: " + host)

sckt.bind(('', port))

sckt.listen(5)

while True:

    conn, address = sckt.accept()

    print("\nConnected with: " + str(address) + "\n")

    file = open("duck.jpg", "wb")

    data = conn.recv(buffSize)

    while data:
        file.write(data)
        print("Received " + str(file.tell()) + " bytes...")
        data = conn.recv(buffSize)

    print("\nFile received!\n")

    file.close()
    conn.close()
