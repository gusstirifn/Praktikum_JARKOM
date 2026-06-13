# Modul 14 802.11 WiFi

**Nama:** Gusti Rifan  
**NIM:** 103072400150  
**Kelas:** IF-04-05  
**Mata Kuliah:** Jaringan Komputer


---

##
Tujuan Praktikum
1. Mahasiswa dapat menginvestigasi cara kerja WiFi menggunakan Wireshark

---

### IEEE 802.11
IEEE 802.11 merupakan standar komunikasi yang digunakan pada jaringan nirkabel atau Wi-Fi. Standar ini mengatur mekanisme komunikasi antara perangkat klien dengan Access Point melalui media udara menggunakan gelombang radio. IEEE 802.11 mendukung berbagai frekuensi operasi seperti 2,4 GHz dan 5 GHz yang banyak digunakan pada jaringan modern.

    - Frekuensi 2.4 GHz
    Kelebihan : Memiliki jangkauan sinyal yang luas dan daya tembus dinding/objek padat yang baik
    Kekurangan : Kecepatan transfer data lebih lambat dan rentan terkena gangguan/interferensi karena spektrumnya lebar dan padat (banyak perangkat rumah tangga menggunakannya).

    - Frekuensi 5 GHz
    Kelebihan : Kecepatan transfer data jauh lebih unggul, interferensi rendah, dan gelombangnya lebih padat.
    Kekurangan : Jangkauan sinyalnya relatif lebih kecil dan sulit menembus penghalang fisik seperti dinding beton.

### Access Point
Access Point (AP) adalah perangkat yang berfungsi sebagai pusat komunikasi dalam jaringan nirkabel. AP memungkinkan perangkat klien seperti laptop, smartphone, dan komputer untuk terhubung ke jaringan lokal maupun internet tanpa menggunakan kabel.

### Beacon Frame
Beacon Frame merupakan salah satu jenis frame manajemen pada IEEE 802.11 yang dikirim secara berkala oleh Access Point. Frame ini berisi informasi penting mengenai jaringan, seperti nama jaringan (SSID), kanal yang digunakan, kecepatan transfer data yang didukung, serta parameter lainnya yang diperlukan perangkat klien untuk menemukan dan terhubung ke jaringan.

Untuk menganalis lebih lanjut praktikum disiapkan dengan mengunduh dan ekstrak berkas ZIP pelacak aktivitas Wireshark dari tautan laboratorium resmi: http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip. Buka berkas pelacakan bernama Wireshark_802_11.pcap menggunakan aplikasi Wireshark.

### Langkah Percobaan
1. Menjalankan aplikasi Wireshark.
2. Buka berkas pelacakan bernama Wireshark_802_11.pcap.
3. Menggunakan filter yang sesuai untuk mengamati paket IEEE 802.11 (wlan.fc.subtype == 8 && wlan.fc.type == 0)

![filterIEEE](/assets/image/M14/filterIEEE.png)

![frame3](/assets/image/M14/frame3.png)

Beacon Frame merupakan frame manajemen yang dikirim secara berkala oleh Access Point untuk mengumumkan keberadaan jaringan nirkabel. Dari hasil pengamatan menggunakan Wireshark, diperoleh beberapa informasi penting sebagai berikut:

    - PHY Type (802.11b (HR/DSSS)): Menunjukkan tipe lapisan fisik nirkabel yang digunakan adalah standar 802.11b berkecepatan tinggi dengan modulasi High-Rate Direct Sequence Spread Spectrum.
    - Short Preamble (False): Menandakan penggunaan Preamble panjang (Long Preamble). Preamble adalah sinkronisasi bagian awal frame. Nilai False berarti sistem memprioritaskan kompatibilitas dengan perangkat lama dibanding optimasi kecepatan.
    - Channel (6) / Frequency (2437MHz) menunjukkan kanal frekuensi yang digunakan untuk komunikasi, beroperasi pada Saluran 6 di spektrum frekuensi 2.4 GHz.
    - Signal Strength / Noise Level: menunjukkan kekuatan sinyal yang diterima oleh perangkat, Kekuatan sinyal yang diterima adalah -30 dBm (sangat kuat/bagus) dengan tingkat gangguan (Noise) berada pada -100 dBm.
    - SSID menunjukkan nama jaringan Wi-Fi yang dipancarkan oleh Access Point, yaitu "30 Munroe St".
    - Beacon Interval menunjukkan periode pengiriman Beacon Frame oleh Access Point.
    - Supported Rates menunjukkan kecepatan transmisi data yang didukung oleh jaringan.

Informasi tersebut digunakan oleh perangkat klien untuk mengenali dan memilih jaringan yang tersedia sebelum melakukan proses koneksi.

4. Mengamati Data Transfer.

![datatransfer](/assets/image/M14/datatransfer.png)

- Frame Number: 480
- Waktu Paket Tertangkap: 24.828253 detik
- Ukuran Frame: 537 bytes (4296 bits)
- Ukuran Header Radiotap: 24 bytes

Artinya paket yang dikirim memiliki total ukuran 537 byte yang berhasil ditangkap sepenuhnya oleh Wireshark.

Paket frame 480 menunjukkan proses request HTTP dari host 192.168.1.109 ke server 128.119.245.12. Klien menggunakan metode GET untuk meminta file /wireshark-labs/alice.txt melalui port 80. Segmen TCP memiliki payload 435 byte dengan Sequence Number dan Acknowledgment Number masing-masing bernilai 1, menandakan komunikasi TCP telah terbentuk dan proses transfer data sedang berlangsung.

5. Mengamati proses Association dan Disassociation antara perangkat klien dan Access Point.

- frame 1750

![frame 1750](/assets/image/M14/frame1750.png)

    - Tipe Frame: Association Request
    - Source Address: Intel_d1:b6:4f
    - Destination Address: CiscoLinksys_f5:ba:bb
    - SSID yang dituju: linksys_SES_24086
Frame ini menunjukkan bahwa perangkat klien Intel mengirimkan permintaan untuk bergabung dengan jaringan WLAN bernama linksys_SES_24086. Pada paket tersebut klien juga mengirimkan informasi kemampuan perangkat seperti Supported Rates (1 Mbps, 2 Mbps, 5.5 Mbps, dan 11 Mbps) serta informasi keamanan WPA.

- frame 2162

![frame 2162](/assets/image/M14/frame2162.png)

    - Tipe Frame: Association Request
    - Source Address: Intel_d1:b6:4f
    - Destination Address: CiscoLinksys_f7:1d:51
    - SSID yang dituju: 30 Munroe St
Frame ini menunjukkan klien mencoba melakukan asosiasi ke Access Point lain dengan SSID 30 Munroe St. Klien menginformasikan dukungan kecepatan hingga 54 Mbps dan fitur Quality of Service (QoS).

paket permintaan asosiasi teratas (Frame 1750) dengan paket asosiasi terbawah (Frame 2162), terjadi perubahan pada bagian parameter SSID:

- Pada Frame 1750, klien mencoba berasosiasi ke AP dengan SSID "linksys_SES_24086".
- Pada Frame 2162 (paling bawah), klien berpindah dan mengirim permintaan asosiasi baru ke AP dengan SSID "30 Munroe St".

- tanggapan Assosiasi dianalisis melalui filter subtype respon: wlan.fc.type_subtype == 1

![tanggapanAssosiasi](/assets/image/M14/tanggapanAssosiasi.png)

Di sini, Transmitter Address diisi oleh MAC Address milik perangkat pengirim respon, yaitu CiscoLinksys_f7:1d:51 , sebagai tanda bahwa Access Point menyetujui permintaan koneksi dari klien (Intel_d1:6b:4f). Karena AP mengirimkan Association Response, maka dapat disimpulkan bahwa permintaan asosiasi telah diproses dan klien diizinkan untuk melanjutkan proses koneksi ke jaringan WLAN.