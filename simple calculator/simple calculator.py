print('SELAMAT DATANG DI KALKULATOR SEDERHANA\n')
print('Apa yang ingin kamu lakukan....')
print('Masukkan angka yang sesuai untuk melakukan operasi!')
print('Masukkan angka 1 untuk penjumlahan')
print('Masukkan angka 2 untuk pengurangan')
print('Masukkan angka 3 untuk perkalian')
print('Masukkan angka 4 untuk pembagian\n')

operasi = int(input('Masukkan angka untuk memilih operasi yang akan dilakukan : '))

if operasi == 1:
    print('Kamu memilih operasi penjumlahan!\n')
    def tambah(a, b):
        hasil = a + b
        return hasil
    a = float(input('Masukkan angka : '))
    b = float(input('Masukkan angka : '))

    penjumlahan1 = tambah(a, b)
    print(f'\nHasil penjumlahan adalah {penjumlahan1}')
    