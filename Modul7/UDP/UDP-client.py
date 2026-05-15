from socket import * ##import all libary
import sys #untuk kontrol sistem (misalnya exit)

serverName = '192.168.0.22' #alamat IP server yang dituju
serverPort = 12000 #port yang dituju

clientSocket = socket(AF_INET, SOCK_DGRAM) #membuat socket ipv4 dgn protokol UDP
clientSocket.settimeout(5)  #batas waktu tunggu 5 detik

print("Ketik 'exit' untuk mematikan server dan keluar, atau 'keluar' untuk tutup client saja.\n")

try:
    while True: #loop untuk input dari user
        message = input('Masukkan kalimat lowercase : ')
        if not message: #jika input kosong maka ulangi
            continue
        clientSocket.sendto(message.encode(), (serverName, serverPort)) #mengirim pesan ke server
        if message.lower() == 'exit': ##untuk mengecek apakah user ingin keluar
            print("Perintah exit dikirim. Mematikan server dan menutup klien...")
            break
        elif message.lower() == 'keluar':
            print("Menutup klien...")
            break
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #menerima balasan dari server
            print(f"Balasan dari Server: {modifiedMessage.decode()}\n")
        except timeout: #menangani error jika server tidak merespon
            print("Kesalahan : Server tidak merespons (Timeout).\n")

except Exception as e:
    print(f"Terjadi kesalahan : {e}")
finally:
    clientSocket.close() #menutup koneksi socket secara permanen saat loop berhenti
    print("Koneksi ditutup.")