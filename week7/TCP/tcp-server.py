from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(
    ('', serverPort)
)

serverSocket.listen(1)
print("[SYSTEM] server TCP siap digunakan")

running = True
while running:
    #menyetuju koneksi dari client
    connectionSocket, addr = serverSocket.accept()

    while True:
        #pesan yang diterima = 10101010
        message = connectionSocket.recv(2048).decode()

        if not message:
            break

        #cek apakah "exit"
        if message.lower() == "exit":
            print("[SYSTEM] client telah keluar")
            running = False
            break

        #memodifikasikan menjadi capslock
        modifiedMessage = message.upper()
        print("[SERVER] diterima: ", modifiedMessage)

        connectionSocket.send(
            modifiedMessage.encode()
        )

    connectionSocket.close()
    
serverSocket.close()