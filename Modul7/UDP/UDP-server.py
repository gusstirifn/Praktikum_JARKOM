from socket import * #import all libary
import sys #untuk kontrol sistem (misalnya exit)

serverPort = 12000 #Membuat socket UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort)) #server aktif di semua IP pada port 12000

print(f"Server UDP siap menerima pesan pada port {serverPort}")
print("Ketik 'exit' dari sisi klien untuk mematikan server secara remote.\n")

try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048) #menerima data dari client
        original_message = message.decode().strip() #mendecode jadi teks
        if original_message.lower() == 'exit': #jika client kirim "exit" maka server berhenti
            print(f"Mematikan server...")
            break
        modifiedMessage = original_message.upper() #mengubah pesan jadi huruf besar
        print(f"Diterima dari {clientAddress[0]}:{clientAddress[1]}: {original_message}")
        print(f"Mengirim balik : {modifiedMessage}") #menampilkan info client dan pesan
        serverSocket.sendto(modifiedMessage.encode(), clientAddress) #mengirim balasan ke client
        
except Exception as e:
    print(f"\nTerjadi kesalahan : {e}")
finally:
    print("Server telah berhenti.")
    serverSocket.close() #menutup server
    sys.exit(0)