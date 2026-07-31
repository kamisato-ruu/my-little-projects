print('\nSELAMAT DATANG DI KALKULATOR SEDERHANA\n')
print('Apa yang ingin kamu lakukan....')
def instruksi():
    print('Masukkan angka yang sesuai untuk melakukan operasi!')
    print('Masukkan angka 1 untuk penjumlahan')
    print('Masukkan angka 2 untuk pengurangan')
    print('Masukkan angka 3 untuk perkalian')
    print('Masukkan angka 4 untuk pembagian')
    print('Masukkan angka -1 untuk keluar dari program\n')
    
def tambah(a, b):
    hasil = a + b
    return hasil
def kurang(a, b):
    hasil = a - b
    return hasil
def kali(a,b):
    hasil = a * b
    return hasil
def bagi(a, b):
    hasil = a / b
    return hasil

def masukkan():
    a = float(input('Masukkan angka : ').replace(',', '.'))
    b = float(input('Masukkan angka : ').replace(',', '.'))
    return a, b


while True:
    instruksi()
    try:
        operasi = int(input('Masukkan angka untuk memilih operasi yang akan dilakukan : '))
    except ValueError:
        print("Error, hanya bisa memasukkan angka!!\n")
        continue

    if operasi == 1:
        print('Kamu memilih operasi penjumlahan!\n')
        a, b = masukkan()
        penjumlahan1 = tambah(a, b)
        print(f'\nHasil penjumlahan adalah {penjumlahan1:g}.\n')

    elif operasi == 2:
        print('Kamu memilih operasi pengurangan!\n')
        a, b = masukkan()
        penngurangan1 = kurang(a, b)
        print(f'\nHasil pengurangan adalah {penngurangan1:g}.\n')

    elif operasi == 3:
        print('Kamu memilih operasi perkalian!\n')
        a, b = masukkan()
        perkalian1 = kali(a, b)
        print(f'\nHasil perkalian adalah {perkalian1:g}.\n')

    elif operasi == 4:
        print('Kamu memilih operasi pembagian!\n')
        a, b = masukkan()
        if b == 0:
            print('Tidak bisa melakukan pembagian dengan 0.\n')
        else:
            pembagian1 = bagi(a, b)
            print(f'\nHasil pembagian adalah {pembagian1:g}.\n')

    elif operasi == -1:
        print('Terima kasih sudah menggunakan program kalkulator sederhana kami.\n')
        break
    
    else:
        print('\nANGKA YANG ANDA MASUKKAN TIDAK SESUAI!!\n')
        
        