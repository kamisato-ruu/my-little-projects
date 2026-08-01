print("\nSELAMAT DATANG DI KALKULATOR SEDERHANA\n")
print("Apa yang ingin kamu lakukan....")


def instruksi():
    print("Masukkan angka yang sesuai untuk melakukan operasi!")
    print("Masukkan angka 1 untuk penjumlahan")
    print("Masukkan angka 2 untuk pengurangan")
    print("Masukkan angka 3 untuk perkalian")
    print("Masukkan angka 4 untuk pembagian")
    print("Masukkan angka -1 untuk keluar dari program\n")


def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        return None  # return None buat tandain error
    return a / b


def masukkan():
    a = float(input("Masukkan angka : ").replace(",", "."))
    b = float(input("Masukkan angka : ").replace(",", "."))
    return a, b


# Dictionary mapping operasi
operasi_dict = {
    1: ("penjumlahan", tambah),
    2: ("pengurangan", kurang),
    3: ("perkalian", kali),
    4: ("pembagian", bagi),
}

instruksi()  # Tampilkan instruksi sekali di awal

while True:
    try:
        operasi = int(
            input("Masukkan angka untuk memilih operasi yang akan dilakukan : ")
        )
    except ValueError:
        print("Error, hanya bisa memasukkan angka!!\n")
        continue

    if operasi == -1:
        print("Terima kasih sudah menggunakan program kalkulator sederhana kami.\n")
        break

    if operasi in operasi_dict:  # Cek apakah operasi ada di dictionary
        nama_operasi, fungsi = operasi_dict[operasi]  # Ambil nama dan fungsi
        print(f"Kamu memilih operasi {nama_operasi}!\n")

        a, b = masukkan()

        # Khusus bagi, handle pembagian dengan 0
        if operasi == 4 and b == 0:
            print("Tidak bisa melakukan pembagian dengan 0.\n")
        else:
            hasil = fungsi(a, b)
            print(f"\nHasil {nama_operasi} adalah {hasil:g}.\n")
    else:
        print("\nANGKA YANG ANDA MASUKKAN TIDAK SESUAI!!\n")
