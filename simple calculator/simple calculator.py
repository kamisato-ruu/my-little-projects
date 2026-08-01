print("\n___SELAMAT DATANG DI KALKULATOR SEDERHANA___\n")


def instruksi():
    print("Kami menyediakan operasi sederhana...")
    print("Masukkan angka 1 untuk melakukan penjumlahan.")
    print("Masukkan angka 2 untuk melakukan pengurangan.")
    print("Masukkan angka 3 untuk melakukan perkalian.")
    print("Masukkan angka 4 untuk melakukan pembagian.")
    print("Masukkan angka -1 untuk keluar dari program.\n")


def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    return a / b


def masukkan():
    while True:
        try:
            a = float(input("Masukkan angka : ").replace(",", "."))
            b = float(input("Masukkan angka : ").replace(",", "."))
        except ValueError:
            print("Error, hanya bisa memasukkan angka.")

        return a, b


memilih_operasi = {
    1: ("penjumlahan", tambah),
    2: ("pengurangan", kurang),
    3: ("perkalian", kali),
    4: ("pembagian", bagi),
}


instruksi()
while True:
    try:
        operasi = int(
            input(
                "Masukkan angka sesuai instruksi untuk memilih operasi yang akan dilakukan : "
            )
        )
    except ValueError:
        print("Error, hanya bisa memasukkan angka.\n")
        continue

    if operasi == -1:
        print("Terimakasih sudah menggunakan kalkulator sederhana kami.\n")
        break
    elif operasi in memilih_operasi:
        nama_operasi, hasil = memilih_operasi[operasi]
        print(f"Kamu memilih operasi {nama_operasi}.\n")

        a, b = masukkan()

        if operasi == 4 and b == 0:
            print("Tidak bisa melakukan pembagian dengan nol.\n")
        else:
            result = hasil(a, b)
            print(f"Hasil {nama_operasi} yaitu {result:g}.\n")

    else:
        print("ERROR, INPUT TIDAK VALID!!\n")
