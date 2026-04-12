# Modul 3 - HTTP

**Nama:** Gusti Rifan  
**NIM:** 103072400150  
**Kelas:** IF-04-05  
**Mata Kuliah:** Jaringan Komputer

---

## 
Tujuan Praktikum 
1. Mahasiswa dapat menginvestigasi cara kerja protokol HTTP menggunakan Wireshark. 
---

### Basic HTTP GET / Response Interaction
1. Membuka wireshark dan memilih interface jaringan WiFi.
![Open wireshark](../assets/image/W3/openws.png)

2. Membuka browser lalu masuk ke link berikut, http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html.
![Open link](../assets/image/W3/openlink.png)

3. Buka wireshark kembali dan ketik http pada pencarian, maka akan muncul 2 paket HTTP utama(GET dan response).
![2 paket HTTP](../assets/image/W3/2paketHTTP.png)

4. Perhatikan baris length info berteks 200 ok (text/html), lalu dapat dilihat hypertext dan Line-based text data.
![HTTP 200 ok](../assets/image/W3/HTTP200ok.png)

![hypertext & Line-based text Data](../assets/image/W3/hypertext&Line-basedData.png)


### HTTP Conditional GET
5. Buka kembali browser dan masuk ke link berikut, http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html.
![open link 2](../assets/image/W3/openlink2.png)

6. Buka kembali wireshark dan ketik http pada pencarian. Perhatikan baris length info 200 ok (text/html),
   lalu lihat hypertext dan Line-based text datanya.
![hypertext & Line-based Data 2](../assets/image/W3/hypertext&Line-basedData2.png)


### Retrieving Long Documents
7. Kembali ke browser dan buka link berikut, http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html.
![Open link 3](../assets/image/W3/openlink3.png)

8. Buka kembali wireshark dan ketik http pada pencarian. Perhatikan baris length info 200 ok (text/html),
   lalu lihat hypertext dan Line-based text datanya.
![hypertext & Line-based Data 3](../assets/image/W3/hypertext%20&%20Line-based%20Data%203.png)

![hypertext & Line-based Data 3.1](../assets/image/W3/line-based%20data%203.png)

![hypertext & Line-based Data 3.2](../assets/image/W3/line-based%20data%203.2.png)


### HTML dengan Embedded Objects
9. Kembali ke browser dan buka link berikut, http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html.
![Open link 4](../assets/image/W3/openlink4.png)

10. Buka kembali wireshark dan ketik http pada pencarian. Perhatikan baris length info 200 ok (text/html),
   lalu lihat hypertext dan Line-based text datanya.
![hypertext & Line-based Data 4](../assets/image/W3/hypertext%20&%20Line-based%20Data%204.png)

### HTTP Authentication 
11. Kembali ke browser dan buka link berikut, http://gaia.cs.umass.edu/wiresharklabs/protected_pages/HTTP-wireshark-file5.html 
![Open link 5](../assets/image/W3/openlink5.png)

12. Masukkan login dengan Username (wireshark-students) dan password (network).
![login](../assets/image/W3/login.png)

13. Login berhasil
![login berhasil](../assets/image/W3/berhasil%20login.png)

14. Buka kembali wireshark dan ketik http pada pencarian. Perhatikan baris length info 200 ok (text/html),
   lalu lihat hypertext dan Line-based text datanya.
![hypertext & Line-based Data 5](../assets/image/W3/hypertext%20&%20Line-based%20Data%205.png)

15. Jika semua sudah selesai kita dapat menekan tombol close maka wireshark akan stop capture dan kita akan menutup wireshark.
![close](../assets/image/W3/close.png)
