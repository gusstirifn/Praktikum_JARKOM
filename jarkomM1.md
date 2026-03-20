# Laporan Praktikum Week 1
Nama       : Gusti Rifan  
NIM        : 103072400150
Kelas      : IF-04-05  
Mata Kuliah: Jaringan Komputer  
__________________________________________

## Modul 1 RUNNING MODUL 
Tujuan Praktikum 
1.	Mahasiswa mengetahui aturan dan sistem pelaksanaan praktikum  
2.	Mahasiswa mengetahui tools yang akan digunakan dan memastikan tools berfungsi dengan baik selama pelaksanaan pratikum  
 

Berikut adalah tahapan instalasi wireshark :
1. Kunjungi situs web resmi Wireshark melalui browser di alamat https://www.wireshark.org/download.html.
2. Unduh installer yang sesuai dengan OS yang digunakan (seperti Windows atau Linux).
3. Setelah unduhan selesai, lalu menjalankan file installer yang telah diunduh.
4. Ikuti panduan instalasi step by step hingga prosesnya berakhir.
Instalasi berjalan tanpa kendala, hanya butuh waktu beberapa menit hingga Wireshark siap digunakan.
### Dokumentasi Instalasi

- Tahap pertama installer akan memasang Wireshark, dengan menekan tombol next.

<img width="497" height="391" alt="Screenshot 2026-03-14 004850" src="https://github.com/user-attachments/assets/e4fb8933-dba9-4d21-a24a-d9e9b83043dc" />


- Pada tahap ini dapat memilih fitur tambahan :

<img width="501" height="391" alt="Screenshot 2026-03-14 004919" src="https://github.com/user-attachments/assets/c791d1ad-2695-41f4-b5fb-bd484f4b816a" />


- Konfigurasi lokasi instalasi :

<img width="496" height="386" alt="Screenshot 2026-03-14 004939" src="https://github.com/user-attachments/assets/7c5a59d2-2550-4b04-8cce-bfebd3b6a1b7" />


- Proses instalasi sedang berjalan:

<img width="502" height="387" alt="Screenshot 2026-03-14 004958" src="https://github.com/user-attachments/assets/45ebdf9c-4a8b-42d1-a2e6-6dd4196692e5" />


- Instalasi berhasil diselesaikan:

<img width="498" height="384" alt="Screenshot 2026-03-14 005140" src="https://github.com/user-attachments/assets/0a3d812d-0594-4beb-88aa-69334ee71467" />


## Modul 2 PENGENALAN TOOLS 
Tujuan Praktikum 
1.	Mahasiswa dapat melakukan instalasi tool yang digunakan (Wireshark). 
2.	Mahasiswa dapat menggunakan tool (Wireshark) untuk menangkap dan mengidentifikasi paket data  

Dengan Wireshark sudah terinstal, fokus pada pengamatan interaksi HTTP GET dan response.
1. Buka aplikasi Wireshark dan pilih interface jaringan aktif (dalam kasus saya, Wi-Fi).
2. Buka browser dan akses URL berikut: http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html. Halaman web tersebut menampilkan pesan singkat: "Congratulations! You've downloaded the first Wireshark lab file!"
3. Kembali ke Wireshark, masukkan kata "http" di kolom filter.
4. Cari entri dengan label "(text/html)" di daftar paket, lalu klik ikon panah untuk memperluas detailnya.
5. Pada bagian "Line-based text data", isi HTML yang diterima :
6. Pada tahap akhir, klik tombol stop capture di menu dan tutup sesi tangkapan tersebut.
Saya belajar lebih dalam tentang mekanisme permintaan HTTP dari browser dan bagaimana respons ditampilkan dalam Wireshark.
### Lampiran
Screenshot-screenshot berikut diambil saat melakukan tugas praktikum:
- Tampilan utama Wireshark ketika pertama diluncurkan:

<img width="1919" height="1030" alt="Screenshot 2026-03-14 005231" src="https://github.com/user-attachments/assets/c3e68d4b-447d-49d8-a7ca-e0e852266744" />

- Daftar paket yang berhasil ditangkap melalui koneksi Wi-Fi:

<img width="1919" height="1010" alt="Screenshot 2026-03-14 005408" src="https://github.com/user-attachments/assets/ad2a48ee-f72e-4b76-bbf6-7698a5901ce1" />

- Tampilan browser yang menunjukkan halaman lab sederhana:

<img width="1919" height="991" alt="Screenshot 2026-03-14 005513" src="https://github.com/user-attachments/assets/9c936016-66b7-435f-b7a3-77d137b94788" />

- Hasil filter paket menggunakan kata kunci "http":

<img width="1918" height="1035" alt="Screenshot 2026-03-02 162037" src="https://github.com/user-attachments/assets/93bf6802-d396-4f01-b145-53bd03f40cca" />

- Isi dari "Line-based text data" yang berisi respons HTML:

<img width="601" height="116" alt="image" src="https://github.com/user-attachments/assets/3d14f817-4ebc-43e3-ae85-d9a20be22003" />
