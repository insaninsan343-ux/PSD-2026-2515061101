class Node:
    def __init__(self, pesanan):
        self.pesanan = pesanan
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_pesanan(self, pesanan):
        new_node = Node(pesanan)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Pesanan '{pesanan}' berhasil dicatat!")

    def tampilkan_pesanan(self):
        if self.head is None:
            print("Belum ada antrean pesanan.")
            return
        print("\n Antrean Saat Ini:")
        temp = self.head
        no = 1
        while temp:
            print(f"{no}. {temp.pesanan}")
            temp = temp.next
            no += 1

    def proses_pesanan(self):
        if self.head is None:
            print("Tidak ada pesanan untuk diproses.")
        else:
            print(f"☕ Pesanan '{self.head.pesanan}' sudah selesai dan siap diambil!")
            self.head = self.head.next


def menu_utama():
    print("\n=== INSHAN CAFE777 ===")
    print("1. Tambah Pesanan")
    print("2. Lihat Antrean")
    print("3. Proses Pesanan Pertama")
    print("4. Keluar")


def main():
    # Daftar menu yang tersedia di kedai
    menu_tersedia = ["Kopi", "Teh", "Latte", "Machiatto"]
    daftar_antrean = LinkedList()

    while True:
        menu_utama()
        try:
            pilihan = int(input("Pilih menu (1-4): "))
        except ValueError:
            print("Harap masukkan angka!")
            continue

        if pilihan == 1:
            print(f"\nMenu yang tersedia: {', '.join(menu_tersedia)}")
            pesanan = input("Mau pesan apa? ").capitalize() # Mengubah input agar huruf depannya kapital

            # Validasi: Apakah pesanan ada di menu_tersedia?
            if pesanan in menu_tersedia:
                daftar_antrean.tambah_pesanan(pesanan)
            else:
                print(f"Mohon Maaf Kaka, '{pesanan}' tidak tersedia di kedai kami,Silahkan Pesan Sesuai Menu Yang kami sediakan Ya")

        elif pilihan == 2:
            daftar_antrean.tampilkan_pesanan()

        elif pilihan == 3:
            daftar_antrean.proses_pesanan()

        elif pilihan == 4:
            print("Terima kasih! Kedai tutup.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
