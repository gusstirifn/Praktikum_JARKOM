from socket import * #import all libary

serverPort = 12000 #membuat socket server dengan TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind( #menghubungkan server ke ke semua IP dan port
    ('', serverPort)
) 

serverSocket.listen(1) #server siap menerima 1 koneksi client
print("[SYSTEM] Server TCP siap digunakan") #menampilkan status server

running = True
while running:
    connectionSocket, addr = serverSocket.accept() #menerima koneksi dari client
    while True:
        message = connectionSocket.recv(2048).decode() #menerima data dari client lalu decode jadi teks
        if not message: #cek jika tidak ada pesan maka keluar loop
            break

        if message.lower() == "exit": #cek jika client kirim "exit", server akan berhenti
            print("[SYSTEM] Client ingin keluar")
            running = False
            break

        modifiedMessage = message.upper() #mengubah pesan jadi huruf besar (CAPS)
        print("[SYSTEM] Diterima: ", modifiedMessage) #menampilkan pesan di server

        connectionSocket.send ( #mengirim kembali ke client
            modifiedMessage.encode()
        )
    connectionSocket.close() #menutup koneksi dan server
serverSocket.close()