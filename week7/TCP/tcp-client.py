
from socket import * # import all

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(
    (serverName, serverPort)
)

print("[SYSTEM] Masukkan Pesan")

running = True
while running:
    #input pesan dari user
    message = input("Pesan: ")
    
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(1024)
    print("Balasan dari Server: ", modifiedMessage.decode())
    if message.lower() == "exit":
        running = False

