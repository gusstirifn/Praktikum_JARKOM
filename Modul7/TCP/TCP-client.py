from socket import * #import all libary
serverName = "localhost" #menentukan alamat server
serverPort = 12000 #menentukan port yg digunakan

clientSocket = socket(AF_INET, SOCK_STREAM) #membuat socket ipv4 dgn protokol TCP
clientSocket.connect( #client mencoba terhubung ke server
    (serverName, serverPort)
)

print("[SYSTEM] Masukkan pesan") #menampilkan intruksi ke user

running = True
while running: #loop agar client terus berjalan
    message = input("> ") #input user
    clientSocket.send(message.encode()) #mengirim pesan ke server dalam bentuk biner
    if message.lower() == "exit": #untuk mengecek apakah user ingin keluar
        print("[SYSTEM] Keluar dari program")
        running = False
        break
    modifiedMessage = clientSocket.recv(2048) #menerima balasan dari server (maks 2048 byte)
    print("[SYSTEM] Pesan: ", modifiedMessage.decode()) #mengubah dari biner ke teks

clientSocket.close() #menutup koneksi socket
print("[SYSTEM] Socket ditutup")