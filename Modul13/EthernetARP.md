# Modul 13 Ethernet and ARP

**Nama:** Gusti Rifan  
**NIM:** 103072400150  
**Kelas:** IF-04-05  
**Mata Kuliah:** Jaringan Komputer


---

##
Tujuan Praktikum
1. Mahasiswa dapat menginvestigasi cara kerja Ethernet dan ARP menggunakan Wireshark

---

### Ethernet

Ethernet merupakan teknologi jaringan yang bekerja pada lapisan Data Link (Layer 2) dalam model OSI. Ethernet digunakan untuk mengirimkan data dalam bentuk frame antar perangkat yang berada dalam satu jaringan lokal (LAN). Setiap perangkat yang terhubung ke jaringan Ethernet memiliki alamat fisik unik yang disebut Media Access Control (MAC) Address. Alamat tersebut digunakan untuk mengidentifikasi perangkat selama proses pertukaran data.

### Address Resolution Protocol (ARP)

Address Resolution Protocol (ARP) adalah protokol yang digunakan untuk menerjemahkan alamat IP menjadi alamat MAC pada jaringan lokal. Protokol ini diperlukan karena proses komunikasi pada lapisan jaringan menggunakan alamat IP, sedangkan proses pengiriman frame Ethernet membutuhkan alamat MAC tujuan.

### Mekanisme Kerja ARP

Proses kerja ARP dimulai ketika suatu host ingin mengirimkan data ke perangkat lain dalam jaringan lokal. Host akan memeriksa ARP Cache untuk mengetahui apakah alamat MAC tujuan telah tersimpan. Jika informasi tersebut belum tersedia, host akan mengirimkan ARP Request secara broadcast kepada seluruh perangkat dalam jaringan. Perangkat yang memiliki alamat IP sesuai dengan permintaan akan mengirimkan ARP Reply yang berisi alamat MAC miliknya. Setelah informasi tersebut diterima, host akan menyimpannya ke dalam ARP Cache dan menggunakan alamat MAC tersebut untuk proses komunikasi berikutnya.

### Langkah Percobaan

1. Membuka Command Prompt (CMD) sebagai Administrator.

2. Menghapus seluruh entri ARP Cache menggunakan perintah: arp -d *

![CMD](/assets/image/M13/CMD.png)

3. Menjalankan aplikasi Wireshark.

4. Memastikan protokol IPv4 telah nonaktif melalui menu Analyze → Enabled Protocols → IPv4.

![WSIpv4](/assets/image/M13/WSipv4.png)

5. Memulai proses packet capture pada antarmuka jaringan yang digunakan.

6. Membuka browser dan mengakses alamat berikut: http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html

![browser](/assets/image/M13/browser.png)

7. Menghentikan proses capture setelah halaman berhasil dimuat.

8. Menggunakan filter arp pada Wireshark untuk menampilkan paket ARP.

![WSarp](/assets/image/M13/WSarp.png)

9. Memilih salah satu paket ARP untuk dianalisis lebih lanjut.

![paketARP](/assets/image/M13/paketARP.png)

Berdasarkan hasil pengamatan menggunakan Wireshark, paket yang dianalisis merupakan paket ARP Request dengan nilai Opcode = Request (1). Paket ini dikirim oleh perangkat yang memiliki alamat IP 192.168.0.9 dan alamat MAC 82:90:f9:b2:23.

Pada paket tersebut terlihat bahwa Target IP Address adalah 192.168.0.1, sedangkan Target MAC Address masih bernilai 00:00:00:00:00:00. Nilai tersebut menunjukkan bahwa pengirim belum mengetahui alamat fisik (MAC Address) dari perangkat tujuan sehingga perlu melakukan proses pencarian menggunakan protokol ARP.

Karena alamat MAC tujuan belum diketahui, paket ARP Request dikirim secara broadcast menggunakan alamat tujuan Ethernet ff:ff:ff:ff:ff. Dengan metode broadcast, seluruh perangkat yang berada dalam jaringan lokal akan menerima permintaan tersebut. Perangkat yang memiliki alamat IP 192.168.0.1 kemudian akan mengirimkan ARP Reply yang berisi alamat MAC miliknya kepada pengirim.

Secara sederhana, pesan ARP Request tersebut dapat diartikan sebagai pertanyaan: "Siapa yang memiliki alamat IP 192.168.0.1? Beritahukan alamat MAC Anda kepada 192.168.0.9." Setelah alamat MAC tujuan diketahui, perangkat pengirim dapat melakukan komunikasi data menggunakan frame Ethernet secara langsung.

Hasil pengamatan ini menunjukkan bahwa ARP berfungsi sebagai mekanisme penerjemahan alamat IP menjadi alamat MAC pada jaringan lokal. Proses ini sangat penting karena komunikasi pada lapisan Data Link menggunakan MAC Address sebagai identitas tujuan pengiriman data.

### Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Address Resolution Protocol (ARP) digunakan untuk memperoleh alamat MAC dari suatu perangkat berdasarkan alamat IP yang diketahui. Melalui Wireshark dapat diamati proses ARP Request yang dikirim secara broadcast ketika perangkat belum mengetahui alamat MAC tujuan. Setelah perangkat tujuan memberikan ARP Reply, informasi tersebut dapat digunakan untuk proses komunikasi data pada jaringan Ethernet. Dengan demikian, ARP memiliki peran penting dalam mendukung komunikasi antar perangkat pada jaringan lokal.