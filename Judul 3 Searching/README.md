# Sistem Inventory Toko — Sequential Search Sentinel

## Judul Program
**Sistem Pencarian Produk Inventory Toko Menggunakan Algoritma Sequential Search Sentinel**

---

## Deskripsi Singkat

Program ini merupakan simulasi sistem inventory toko yang memanfaatkan algoritma **Sequential Search Sentinel** untuk melakukan pencarian data produk secara efisien. Program menyimpan data produk berupa SKU, nama, kategori, stok, dan harga dalam struktur *list of dictionary*, kemudian memungkinkan pengguna mencari produk berdasarkan **SKU** maupun **Nama Produk** melalui menu interaktif di terminal.

Algoritma Sequential Search Sentinel bekerja dengan cara menambahkan nilai target sementara (sentinel) di akhir list sebelum proses pencarian dimulai. Teknik ini menghilangkan kebutuhan pengecekan kondisi batas array (`i < n`) di setiap iterasi loop, sehingga jumlah perbandingan per iterasi berkurang dari dua menjadi satu. Setelah pencarian selesai, sentinel dihapus, dan program memeriksa apakah indeks hasil pencarian lebih kecil dari panjang data asli untuk menentukan apakah data benar-benar ditemukan.

---

## Source Code

<img width="887" height="456" alt="kode 1- 22 2026-04-23 204644" src="https://github.com/user-attachments/assets/68b1be78-80fd-4eb7-8a94-dded7c5e7c59" />
<img width="887" height="405" alt="kode 23- 44 2026-04-23 204815" src="https://github.com/user-attachments/assets/eb39a49d-d51c-4f12-bd9b-105b0932ae05" />
<img width="894" height="388" alt="kode 45-64 2026-04-23 204948" src="https://github.com/user-attachments/assets/4aa387ed-2ed2-4378-be67-e5a7423d3797" />
<img width="837" height="289" alt="kode 65-79 2026-04-23 205034" src="https://github.com/user-attachments/assets/78dc4bf2-aab3-4115-8dcd-6201d282ad11" />
<img width="894" height="559" alt="kode 80-108 2026-04-23 205132" src="https://github.com/user-attachments/assets/f7b54b16-22f5-484c-94a5-ea79bcc31c75" />
<img width="855" height="192" alt="kode 109-selesai 2026-04-23 205233" src="https://github.com/user-attachments/assets/e56637db-99f2-4437-8773-8da904e2b0a5" />


### Penjelasan Logika Kode Per Bagian

---

### 1. Fungsi `sequential_search_sentinel_by_sku` dan `sequential_search_sentinel_by_name`

```python
def sequential_search_sentinel_by_sku(data, n, target):
    data.append(target)   # (1)
    i = 0                 # (2)
    while data[i] != target:  # (3)
        i += 1            # (4)
    data.pop()            # (5)
    if i < n:             # (6)
        return True, i    # (7)
    else:
        return False, -1  # (8)
```

| Baris | Penjelasan |
|-------|-----------|
| (1) `data.append(target)` | Menambahkan nilai **sentinel** (nilai target) ke posisi paling akhir list. Ini menjamin bahwa loop PASTI berhenti, sehingga tidak perlu cek batas `i < n` di dalam loop. |
| (2) `i = 0` | Inisialisasi indeks pencarian dari posisi pertama (indeks 0). |
| (3) `while data[i] != target` | Loop terus berjalan selama elemen pada indeks `i` tidak sama dengan target. Hanya ada **satu kondisi** di sini — inilah keunggulan sentinel. |
| (4) `i += 1` | Geser indeks ke elemen berikutnya. |
| (5) `data.pop()` | Hapus sentinel yang tadi ditambahkan agar list kembali ke kondisi semula. |
| (6) `if i < n` | Cek apakah loop berhenti **sebelum** posisi sentinel. Jika iya, berarti target ditemukan di data asli. |
| (7) `return True, i` | Kembalikan nilai `True` dan indeks tempat target ditemukan. |
| (8) `return False, -1` | Jika `i == n`, berarti loop berhenti tepat di posisi sentinel → data **tidak ditemukan**. |

> Fungsi `sequential_search_sentinel_by_name` memiliki logika yang **identik**, perbedaannya hanya pada konteks penggunaannya (pencarian berdasarkan nama produk).

---

### 2. Fungsi `tampilkan_semua_produk(data)`

```python
def tampilkan_semua_produk(data):
    print("\n" + "=" * 60)
    print(f"{'NO':<5} {'SKU':<10} {'NAMA PRODUK':<20} ...")
    print("=" * 60)
    for i, produk in enumerate(data):
        print(f"{i+1:<5} {produk['sku']:<10} {produk['nama']:<20} ...")
    print("=" * 60)
```

Fungsi ini mencetak seluruh data produk dalam format tabel yang rapi ke terminal. `enumerate(data)` digunakan untuk mendapatkan nomor urut dan data produk sekaligus. Format string `:<5`, `:<10`, `:<20` berfungsi untuk meratakan teks ke kiri dengan lebar kolom tertentu agar tampilan tabel konsisten.

---

### 3. Fungsi `tampilkan_detail_produk(produk, index)`

```python
def tampilkan_detail_produk(produk, index):
    print(f"  Indeks      : {index}")
    print(f"  SKU         : {produk['sku']}")
    print(f"  Nama Produk : {produk['nama']}")
    ...
```

Fungsi ini menampilkan informasi lengkap produk yang berhasil ditemukan, termasuk indeks posisinya di dalam list, SKU, nama, kategori, jumlah stok, dan harga.

---

### 4. Fungsi `main()`

```python
def main():
    data = [ {"sku": "SKU001", "nama": "Indomie Goreng", ...}, ... ]  # (A)
    n = len(data)                                                       # (B)
    tampilkan_semua_produk(data)                                        # (C)

    pilihan = int(input("Masukkan pilihan (1/2): "))                   # (D)

    if pilihan == 1:                                                    # (E)
        sku_list = [produk["sku"] for produk in data]                  # (F)
        found, index = sequential_search_sentinel_by_sku(sku_list, n, target)
    else:
        nama_list = [produk["nama"] for produk in data]                # (G)
        found, index = sequential_search_sentinel_by_name(nama_list, n, target)

    if found:
        tampilkan_detail_produk(data[index], index)                    # (H)
    else:
        print("Tidak ditemukan")
```

| Label | Penjelasan |
|-------|-----------|
| (A) `data` | List of dictionary berisi 10 produk toko. Setiap produk memiliki key: `sku`, `nama`, `kategori`, `stok`, `harga`. |
| (B) `n = len(data)` | Menyimpan panjang data asli sebelum sentinel ditambahkan, digunakan sebagai pembanding di fungsi pencarian. |
| (C) `tampilkan_semua_produk` | Menampilkan seluruh produk dalam format tabel agar pengguna tahu data apa yang tersedia. |
| (D) Input pilihan | Pengguna memilih metode pencarian: `1` untuk SKU, `2` untuk Nama Produk. Dilindungi dengan `try-except` agar input tidak valid tidak menyebabkan crash. |
| (E-G) Ekstraksi list | Karena sentinel hanya bisa membandingkan satu nilai skalar, data produk perlu diekstrak menjadi list khusus (`sku_list` / `nama_list`) sebelum dikirim ke fungsi pencarian. |
| (H) Tampilkan hasil | Jika `found = True`, data produk ditampilkan lengkap menggunakan `data[index]` yang mengakses dictionary produk di posisi yang ditemukan. |

---

## Output Program

<img width="445" height="335" alt="image" src="https://github.com/user-attachments/assets/560c2e1f-b7b3-4ac8-a31c-e9b2dbe50683" />
<img width="584" height="615" alt="image" src="https://github.com/user-attachments/assets/e5bd922e-df04-4fad-af6d-91c7e14aeac0" />
<img width="534" height="521" alt="image" src="https://github.com/user-attachments/assets/45926ca3-dc41-4311-a6ee-9d870798a50a" />


### Contoh Output — Pencarian Berdasarkan SKU (Ditemukan)

```
============================================================
     SISTEM INVENTORY TOKO - SEQUENTIAL SEARCH SENTINEL
============================================================

============================================================
NO    SKU        NAMA PRODUK          KATEGORI     STOK     HARGA
============================================================
1     SKU001     Indomie Goreng       Makanan      150      Rp3,500
2     SKU002     Aqua 600ml           Minuman      200      Rp4,000
3     SKU003     Sabun Lifebuoy       Kebersihan   80       Rp12,000
...
============================================================

Pilih metode pencarian:
  1. Cari berdasarkan SKU
  2. Cari berdasarkan Nama Produk

Masukkan pilihan (1/2): 1

Masukkan SKU yang ingin dicari (contoh: SKU003): SKU003

✅ PRODUK DITEMUKAN!
----------------------------------------
  Indeks      : 2
  SKU         : SKU003
  Nama Produk : Sabun Lifebuoy
  Kategori    : Kebersihan
  Stok        : 80 pcs
  Harga       : Rp12,000
----------------------------------------
```

### Contoh Output — Pencarian Berdasarkan Nama (Tidak Ditemukan)

```
Masukkan pilihan (1/2): 2

Masukkan nama produk yang ingin dicari (contoh: Aqua 600ml): Mie Sedaap

❌ Produk 'Mie Sedaap' tidak ditemukan dalam inventory.
```

**Penjelasan Output:**
- Program menampilkan seluruh tabel produk terlebih dahulu saat dijalankan.
- Pengguna memilih metode pencarian (SKU atau nama).
- Jika ditemukan, program menampilkan detail lengkap produk beserta indeksnya di dalam list.
- Jika tidak ditemukan, program menampilkan pesan yang informatif tanpa error.

---

## Link YouTube

> 🎥 *(https://youtu.be/xxb9S6arnMg?si=XbssEILEy_azJgSg)*
