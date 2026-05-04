# a. Judul Program
Pengurutan Saldo Nasabah Menggunakan Algoritma Exchange Sort (Descending)

# b. Deskripsi Singkat
Program ini adalah sebuah aplikasi berbasis terminal (CLI) yang berfungsi untuk menerima dan mengelola data saldo nasabah bank. Pengguna dapat memasukkan jumlah nasabah secara dinamis, lalu program akan meminta input nominal saldo untuk masing-masing nasabah. Program ini juga dilengkapi dengan validasi input untuk mencegah *error* jika pengguna memasukkan karakter selain angka.

Algoritma yang diterapkan dalam program ini adalah **Exchange Sort** dengan pengurutan secara *Descending* (dari nilai terbesar ke terkecil). Struktur data utama yang digunakan adalah *Array* (menggunakan tipe data List pada Python) untuk menyimpan daftar saldo nasabah tersebut, yang memungkinkan manipulasi dan pertukaran indeks elemen secara langsung selama proses *sorting* berlangsung.

# c. Source Code

<img width="740" height="361" alt="image" src="https://github.com/user-attachments/assets/022d3c8a-0914-4b15-a98b-1c4c281d58a3" />
<img width="845" height="420" alt="image" src="https://github.com/user-attachments/assets/d521c707-8fe6-47b9-adc3-7e777f585dd1" />
<img width="715" height="55" alt="image" src="https://github.com/user-attachments/assets/6af62717-a9bf-4fef-ac17-30f2357fcfc8" />



**Penjelasan Logika Berjalannya Kode Program:**
* `def tukar(arr, i, j):` : Mendeklarasikan fungsi bantuan untuk menukar posisi dua elemen di dalam array.
* `temp = arr[i]` : Menyimpan nilai array indeks ke-i ke dalam variabel sementara (`temp`).
* `arr[i] = arr[j]` : Mengganti nilai array indeks ke-i dengan nilai dari array indeks ke-j.
* `arr[j] = temp` : Mengisi array indeks ke-j dengan nilai yang ada di variabel `temp`.
* `def exchange_sort(arr, n):` : Mendeklarasikan fungsi utama algoritma Exchange Sort.
* `for i in range(n - 1):` : Perulangan luar yang berjalan dari elemen pertama hingga elemen sebelum terakhir untuk dijadikan titik perbandingan.
* `for j in range(i + 1, n):` : Perulangan dalam yang membandingkan elemen ke-i dengan seluruh elemen setelahnya (ke-j).
* `if arr[i] < arr[j]:` : Logika *Descending*. Jika elemen saat ini lebih kecil dari elemen di sebelah kanannya, maka...
* `tukar(arr, i, j)` : Memanggil fungsi `tukar` untuk menukar posisi kedua elemen tersebut agar nilai yang lebih besar pindah ke depan.
* `def main():` : Mendeklarasikan fungsi utama yang mengatur alur input dan output.
* `try ... except ValueError:` : Blok validasi (error handling) untuk memastikan input `n` (jumlah nasabah) adalah bilangan bulat.
* `arr = []` : Mendeklarasikan list (array) kosong untuk menampung data saldo nasabah.
* `for i in range(n):` : Melakukan perulangan sebanyak jumlah nasabah untuk meminta input saldo.
* `nilai = float(input(...))` : Meminta input saldo dan mengubahnya menjadi tipe data `float` agar mendukung angka desimal.
* `arr.append(nilai)` : Memasukkan nilai saldo yang dinputkan ke dalam array `arr`.
* `print(f"\nSaldo nasabah sebelum diurutkan: {arr}")` : Menampilkan isi array saldo yang masih acak (belum terurut).
* `exchange_sort(arr, n)` : Memanggil fungsi `exchange_sort` untuk memulai proses pengurutan array `arr`.
* `for i in range(n): print(arr[i], end=" ")` : Mencetak isi array yang sudah terurut ke layar secara mendatar (*horizontal*).
* `if __name__ == "__main__": main()` : Blok penanda eksekusi utama yang akan memanggil fungsi `main()` saat file Python dijalankan.

# d. Output Program

<img width="535" height="110" alt="image" src="https://github.com/user-attachments/assets/88d235c4-c1d5-4712-a5cd-c737e5e05114" />
<img width="937" height="104" alt="image" src="https://github.com/user-attachments/assets/c4898430-f8b5-43f7-8a17-2416846ff1b8" />


**Penjelasan Output Program:**
Pada saat program dijalankan, program pertama kali meminta pengguna memasukkan jumlah nasabah (misalnya 6). Kemudian program meminta nominal saldo nasabah satu per satu. Output menunjukkan array awal: `[2000000.0, 8000000.0, 10000000.0, 1000000.0, 3000000.0, 500000.0]`. Setelah diproses oleh algoritma Exchange Sort, output akhir menampilkan hasil di mana data saldo tersebut telah berhasil disusun secara berurutan dari nominal yang paling besar ke nominal yang paling kecil, yaitu menjadi `10000000.0 8000000.0 3000000.0 2000000.0 1000000.0 500000.0 `.

# e. Link YouTube

[Klik di sini untuk menonton Video Presentasi / Demo Kode Program]https://youtu.be/48XCR9Y68D4?si=iuLJfyeblmF8u-gM
