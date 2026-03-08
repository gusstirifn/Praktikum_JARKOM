# Laporan Praktikum Week 1
Nama       : Gusti Rifan  
NIM        : 103072400150
Kelas      : IF-04-05  
Mata Kuliah: Jaringan Komputer  
__________________________________________
## Instalasi Wireshark (modul 1)
Awal dari praktikum ini dimulai dengan instalasi Wireshark. Ini adalah langkah penting agar bisa melanjutkan ke tugas-tugas berikutnya. Berikut adalah prosedur yang saya lakukan:
1. Kunjungi situs web resmi Wireshark melalui browser di alamat https://www.wireshark.org/download.html.
2. Unduh installer yang sesuai dengan OS yang digunakan (seperti Windows atau Linux), pastikan memilih versi stabil terbaru.
3. Setelah unduhan selesai, klik dua kali pada file installer untuk menjalankannya.
4. Ikuti panduan instalasi step by step hingga prosesnya berakhir; tentukan folder instalasi dan tunggu sampai selesai.
Instalasi berjalan tanpa kendala, hanya butuh waktu beberapa menit hingga Wireshark siap digunakan.
### Dokumentasi Instalasi
Saya mengambil beberapa screenshot selama proses instalasi untuk dokumentasi:
- Halaman download Wireshark:

![WhatsApp Image 2026-03-09 at 00 52 08 (10)](https://github.com/user-attachments/assets/877c132a-1817-487a-904a-b127833aa970)

- Langkah awal setup:

![WhatsApp Image 2026-03-09 at 00 52 08 (8)](https://github.com/user-attachments/assets/c9c13184-2a95-4f31-b61c-1b7a7617f3bc)

- Persetujuan lisensi:

![WhatsApp Image 2026-03-09 at 00 52 08 (6)](https://github.com/user-attachments/assets/881695d7-7a40-422a-b494-3d0d9ac02659)

- Pemilihan fitur yang akan diinstal:

![WhatsApp Image 2026-03-09 at 00 52 08 (5)](https://github.com/user-attachments/assets/6ece5ced-4474-40d1-b339-708d5db69951)

- Konfigurasi lokasi instalasi:

![WhatsApp Image 2026-03-09 at 00 52 08 (4)](https://github.com/user-attachments/assets/a05043fc-cafd-45f9-a1f7-8a5184739f36)

- Proses instalasi sedang berjalan:

![WhatsApp Image 2026-03-09 at 00 52 08 (3)](https://github.com/user-attachments/assets/30190055-b02c-4e79-940c-4bedffbcec15)

![WhatsApp Image 2026-03-09 at 00 52 08 (2)](https://github.com/user-attachments/assets/0aba776b-5af2-4a2f-951f-1240aa64cdfb)

![WhatsApp Image 2026-03-09 at 00 52 08 (1)](https://github.com/user-attachments/assets/39ebd652-aa7c-4398-b416-29014c0b4bf6)

- Penambahan komponen WinPcap/Npcap:

![WhatsApp Image 2026-03-09 at 00 52 08](https://github.com/user-attachments/assets/cfd60a8d-93fe-4fec-b4b0-a88ae7b948f9)

- Tahap akhir instalasi:

![WhatsApp Image 2026-03-09 at 00 52 07](https://github.com/user-attachments/assets/1d08cf67-d762-4413-a4f3-3e0b8aa3c1ed)

- Instalasi berhasil diselesaikan:

![WhatsApp Image 2026-03-09 at 00 52 08 (9)](https://github.com/user-attachments/assets/2748d1fb-960b-4e9a-8958-6ccf0878d69a)

## Tugas Praktikum Week 1 (modul 2)
Dengan Wireshark sudah terinstal, saya lanjut ke bagian kedua modul 2 yang fokus pada pengamatan interaksi HTTP GET dan response.
1. Buka aplikasi Wireshark dan pilih interface jaringan aktif (dalam kasus saya, Wi-Fi). Pastikan VPN dimatikan jika sedang aktif untuk menghindari gangguan dalam penangkapan paket.
2. Buka browser dan akses URL berikut: http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html. Halaman web tersebut menampilkan pesan singkat: "Congratulations! You've downloaded the first Wireshark lab file!"
3. Kembali ke Wireshark, masukkan kata "http" di kolom filter tanpa tanda kutip, kemudian tekan Enter untuk memfilter paket HTTP saja.
4. Cari entri dengan label "(text/html)" di daftar paket, lalu klik ikon panah untuk memperluas detailnya.
5. Pada bagian "Line-based text data", isi HTML yang diterima terlihat seperti ini:
6. Untuk mengakhiri, klik tombol stop capture di menu dan tutup sesi tangkapan tersebut.
Melalui aktivitas ini, saya belajar lebih dalam tentang mekanisme permintaan HTTP dari browser dan bagaimana respons ditampilkan dalam Wireshark.
### Lampiran
Screenshot-screenshot berikut diambil saat melakukan tugas praktikum:
- Antarmuka utama Wireshark setelah aplikasi diluncurkan:

![WhatsApp Image 2026-03-09 at 00 52 08 (11)](https://github.com/user-attachments/assets/3d8f21f0-5bf9-46ff-ae69-0133e4df1c9e)
  
- Daftar paket yang berhasil ditangkap melalui koneksi Wi-Fi:

![WhatsApp Image 2026-03-09 at 00 52 08 (13)](https://github.com/user-attachments/assets/9d0c8dc2-1ffd-4e89-80a5-ca2bdb29fa7d)

- Tampilan browser yang menunjukkan halaman lab sederhana:

![WhatsApp Image 2026-03-09 at 00 52 08 (14)](https://github.com/user-attachments/assets/538f8602-1b71-4ae9-8c28-983d024b0fa0)

- Hasil filter paket menggunakan kata kunci "http":

![WhatsApp Image 2026-03-09 at 00 52 08 (12)](https://github.com/user-attachments/assets/e4ecc729-4b97-4939-a2ed-18ea8a2cd9f9)

- Isi dari "Line-based text data" yang berisi respons HTML:

![WhatsApp Image 2026-03-09 at 00 52 10](https://github.com/user-attachments/assets/1917ed66-fa1c-458f-9d0d-51e7a814e950)
