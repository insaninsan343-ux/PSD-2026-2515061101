# Judul Program: Sistem Antrean Pesanan "INSHAN CAFE777" (Implementasi Linked List)

## Deskripsi Singkat
Program ini adalah sebuah sistem manajemen antrean sederhana berbasis *Command Line Interface* (CLI) yang dirancang untuk kedai kopi bernama "INSHAN CAFE777". Sistem ini berfungsi untuk mencatat pesanan pelanggan yang masuk, menampilkan daftar antrean pesanan saat ini, dan memproses pesanan tersebut secara berurutan. Program ini juga dilengkapi dengan validasi menu, di mana pelanggan hanya dapat memesan minuman yang tersedia di dalam daftar menu kedai.

Untuk menjalankan fungsinya, program ini menerapkan algoritma struktur data **Singly Linked List**. Pendekatan ini dipilih karena *Linked List* sangat efisien dalam menambahkan data baru secara dinamis tanpa perlu menentukan ukuran memori di awal. Program ini mengimplementasikan konsep antrean FIFO (*First-In, First-Out*), di mana pesanan yang pertama kali masuk (berada di posisi *head* pada *Linked List*) akan menjadi pesanan pertama yang diproses dan dikeluarkan dari antrean.

## Source Code
<img width="1366" height="728" alt="1 py - python sd - Visual Studio Code 16_04_2026 00_27_41" src="https://github.com/user-attachments/assets/306a0773-ba28-431f-b457-450a6204246b" />
<img width="1366" height="728" alt="1 py - python sd - Visual Studio Code 16_04_2026 00_28_16" src="https://github.com/user-attachments/assets/925b34d0-eeb9-4caf-91ae-33e56df72573" />
<img width="1366" height="728" alt="1 py - python sd - Visual Studio Code 16_04_2026 00_28_47" src="https://github.com/user-attachments/assets/c060676b-7296-43d1-b280-271e04793a33" />


**Penjelasan Logika Kode Program:**

1. **`class Node:`** 
   - `def __init__(self, pesanan):` Konstruktor untuk membuat simpul (*node*) baru. Parameter `pesanan` menyimpan nama minuman yang dipesan, sedangkan `self.next = None` berfungsi sebagai *pointer* yang menunjuk ke *node* selanjutnya (awalnya kosong).
2. **`class LinkedList:`**
   - `def __init__(self):` Menginisialisasi *Linked List* dengan mengatur `self.head = None`, menandakan antrean masih kosong.
   - `def tambah_pesanan(self, pesanan):` Membuat `new_node` dari pesanan baru. Jika antrean kosong (`self.head is None`), *node* ini langsung menjadi *head*. Jika tidak, program akan melakukan *looping* (`while temp.next`) untuk mencari *node* terakhir dan menyambungkan `new_node` di bagian ekor (*tail*).
   - `def tampilkan_pesanan(self):` Mengecek apakah antrean kosong. Jika ada pesanan, program akan melakukan *traverse* (menelusuri) dari *head* hingga *node* terakhir menggunakan `while temp:`, lalu mencetak setiap pesanan beserta nomor urutnya.
   - `def proses_pesanan(self):` Mengambil pesanan pada urutan pertama. Jika antrean tidak kosong, program mencetak nama pesanan pada `self.head`, lalu menghapus pesanan tersebut dari antrean dengan cara menggeser *head* ke *node* berikutnya (`self.head = self.head.next`).
3. **Fungsi `menu_utama()`:**
   - Mencetak antarmuka menu pilihan (1-4) agar mudah dibaca oleh pengguna.
4. **Fungsi `main()`:**
   - Mendeklarasikan `menu_tersedia` (Kopi, Teh, Latte, Machiatto) dan menginisialisasi objek `daftar_antrean`.
   - Menggunakan perulangan `while True` agar program terus berjalan hingga pengguna memilih keluar.
   - Terdapat blok `try-except` untuk memastikan pengguna hanya memasukkan angka (1-4).
   - **Pilihan 1:** Meminta input pesanan. Terdapat validasi `if pesanan in menu_tersedia:` untuk memastikan minuman ada di menu. Fungsi `.capitalize()` digunakan agar format huruf sesuai. Jika valid, pesanan masuk ke *Linked List*.
   - **Pilihan 2:** Memanggil metode `tampilkan_pesanan()`.
   - **Pilihan 3:** Memanggil metode `proses_pesanan()`.
   - **Pilihan 4:** Menghentikan program dengan perintah `break`.

## Output Program

<img width="1015" height="266" alt="1 py - python sd - Visual Studio Code 16_04_2026 00_43_35" src="https://github.com/user-attachments/assets/6e358f4e-e1e8-4ad7-8a14-473b7eaf7652" />
<img width="1019" height="263" alt="1 py - python sd - Visual Studio Code 16_04_2026 00_44_29" src="https://github.com/user-attachments/assets/08ec83cf-595a-49a5-ab95-5a83f853905c" />
<img width="1015" height="259" alt="1 py - python sd - Visual Studio Code 16_04_2026 00_44_39" src="https://github.com/user-attachments/assets/a7038a00-be1c-4465-9cdf-1f41f0d4e991" />
<img width="1022" height="266" alt="1 py - python sd - Visual Studio Code 16_04_2026 00_44_48" src="https://github.com/user-attachments/assets/1648ce75-56e4-44a7-a305-30f268eb8a05" />
<img width="1003" height="261" alt="1 py - python sd - Visual Studio Code 16_04_2026 00_44_59" src="https://github.com/user-attachments/assets/2d35b17b-bb13-4a9c-985e-c7af2ec75251" />
<img width="1019" height="268" alt="1 py - python sd - Visual Studio Code 16_04_2026 00_45_08" src="https://github.com/user-attachments/assets/ce842386-41fa-4341-a4c1-43c167d431b8" />

**Penjelasan Output Program:**
- Saat program dijalankan, pengguna akan melihat daftar menu utama.
- Jika pengguna memilih opsi **1**, program akan menampilkan menu minuman yang tersedia. Jika pengguna memasukkan pesanan yang sesuai (misal: "Kopi"), program akan mencetak "Pesanan 'Kopi' berhasil dicatat!". Jika pengguna memasukkan pesanan di luar menu (misal: "Susu"), program akan menampilkan pesan penolakan yang ramah.
- Jika pengguna memilih opsi **2**, program akan menampilkan daftar pesanan secara berurutan (misal: 1. Kopi, 2. Teh). Jika belum ada pesanan, akan muncul pesan peringatan bahwa antrean kosong.
- Jika pengguna memilih opsi **3**, program akan mengambil pesanan nomor 1 (Kopi) dan mencetak pesan bahwa pesanan tersebut sudah selesai. Saat opsi 2 dicek kembali, pesanan Kopi sudah hilang dari daftar antrean.
- Jika pengguna memasukkan huruf (bukan angka) pada pilihan menu, program akan memberikan peringatan "Harap masukkan angka!" dan mengulang menu utama.
- Memilih opsi **4** akan mencetak pesan penutup dan memberhentikan eksekusi program.

## Link YouTube

https://youtu.be/tO-1qlH_rn8?si=y-iPhx3_tzhcGz2s
