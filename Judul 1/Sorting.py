def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def exchange_sort(arr, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Ubah tanda > menjadi < untuk mengurutkan dari terbesar ke terkecil
            if arr[i] < arr[j]:
                tukar(arr, i, j)

def main():
    try:
        n = int(input("Masukkan jumlah nasabah: "))
    except ValueError:
        print("Input tidak valid!")
        return
        
    arr = []
    print("Masukkan nominal saldo nasabah:")
    for i in range(n):
        while True:
            try:
                # Menggunakan float agar mendukung nilai nominal desimal/pecahan uang, 
                # (kamu bisa ganti ke int() lagi jika asisten praktikum mewajibkan bilangan bulat)
                nilai = float(input(f"Saldo nasabah ke-{i+1}: "))
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
                
    print(f"\nSaldo nasabah sebelum diurutkan: {arr}")
    
    exchange_sort(arr, n)
    
    print("Saldo nasabah setelah diurutkan (Exchange Sort - Descending):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    main()
