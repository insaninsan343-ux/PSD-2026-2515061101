def sequential_search_sentinel_by_sku(data, n, target):
    data.append(target)
    i = 0
    while data[i] != target:
        i += 1
    data.pop()
    if i < n:
        return True, i
    else:
        return False, -1


def sequential_search_sentinel_by_name(data, n, target):
    data.append(target)
    i = 0
    while data[i] != target:
        i += 1
    data.pop()
    if i < n:
        return True, i
    else:
        return False, -1


def tampilkan_semua_produk(data):
    print("\n" + "=" * 60)
    print(f"{'NO':<5} {'SKU':<10} {'NAMA PRODUK':<20} {'KATEGORI':<12} {'STOK':<8} {'HARGA'}")
    print("=" * 60)
    for i, produk in enumerate(data):
        print(f"{i+1:<5} {produk['sku']:<10} {produk['nama']:<20} {produk['kategori']:<12} {produk['stok']:<8} Rp{produk['harga']:,}")
    print("=" * 60)


def tampilkan_detail_produk(produk, index):
    print("\n✅ PRODUK DITEMUKAN!")
    print("-" * 40)
    print(f"  Indeks      : {index}")
    print(f"  SKU         : {produk['sku']}")
    print(f"  Nama Produk : {produk['nama']}")
    print(f"  Kategori    : {produk['kategori']}")
    print(f"  Stok        : {produk['stok']} pcs")
    print(f"  Harga       : Rp{produk['harga']:,}")
    print("-" * 40)


def main():
    data = [
        {"sku": "SKU001", "nama": "Indomie Goreng",   "kategori": "Makanan",   "stok": 150, "harga": 3500},
        {"sku": "SKU002", "nama": "Aqua 600ml",        "kategori": "Minuman",   "stok": 200, "harga": 4000},
        {"sku": "SKU003", "nama": "Sabun Lifebuoy",    "kategori": "Kebersihan","stok": 80,  "harga": 12000},
        {"sku": "SKU004", "nama": "Susu Ultra 250ml",  "kategori": "Minuman",   "stok": 60,  "harga": 6500},
        {"sku": "SKU005", "nama": "Roti Tawar Sari",   "kategori": "Makanan",   "stok": 30,  "harga": 18000},
        {"sku": "SKU006", "nama": "Shampoo Pantene",   "kategori": "Kebersihan","stok": 45,  "harga": 27000},
        {"sku": "SKU007", "nama": "Teh Botol Sosro",   "kategori": "Minuman",   "stok": 120, "harga": 5000},
        {"sku": "SKU008", "nama": "Minyak Goreng 1L",  "kategori": "Makanan",   "stok": 75,  "harga": 21000},
        {"sku": "SKU009", "nama": "Deterjen Rinso",    "kategori": "Kebersihan","stok": 55,  "harga": 19000},
        {"sku": "SKU010", "nama": "Kopi Kapal Api",    "kategori": "Minuman",   "stok": 90,  "harga": 8000},
    ]
    n = len(data)

    print("=" * 60)
    print("     SISTEM INVENTORY TOKO - SEQUENTIAL SEARCH SENTINEL")
    print("=" * 60)

    tampilkan_semua_produk(data)

    print("\nPilih metode pencarian:")
    print("  1. Cari berdasarkan SKU")
    print("  2. Cari berdasarkan Nama Produk")

    while True:
        try:
            pilihan = int(input("\nMasukkan pilihan (1/2): "))
            if pilihan in [1, 2]:
                break
            else:
                print("Pilihan tidak valid, masukkan 1 atau 2!")
        except ValueError:
            print("Input tidak valid, masukkan angka 1 atau 2!")

    if pilihan == 1:
        # Cari berdasarkan SKU
        sku_list = [produk["sku"] for produk in data]
        n_sku = len(sku_list)

        while True:
            target = input("\nMasukkan SKU yang ingin dicari (contoh: SKU003): ").strip().upper()
            if target:
                break
            print("Input tidak boleh kosong!")

        found, index = sequential_search_sentinel_by_sku(sku_list, n_sku, target)

        if found:
            tampilkan_detail_produk(data[index], index)
        else:
            print(f"\n❌ Produk dengan SKU '{target}' tidak ditemukan dalam inventory.")

    else:
        # Cari berdasarkan Nama Produk
        nama_list = [produk["nama"] for produk in data]
        n_nama = len(nama_list)

        while True:
            target = input("\nMasukkan nama produk yang ingin dicari (contoh: Aqua 600ml): ").strip()
            if target:
                break
            print("Input tidak boleh kosong!")

        found, index = sequential_search_sentinel_by_name(nama_list, n_nama, target)

        if found:
            tampilkan_detail_produk(data[index], index)
        else:
            print(f"\n❌ Produk '{target}' tidak ditemukan dalam inventory.")


if __name__ == "__main__":
    main()
