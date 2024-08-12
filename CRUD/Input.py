def pilihan_user(banyak_pilihan) -> int:
    while True:
        try:
            hasil = int(input('\nMasukkan pilihan: '))
            if hasil > -1 and hasil < (banyak_pilihan):
                break
            else:
                print('Tolong masukkan pilihan yang valid.')
        except:
            print('Tolong masukkan angka.')
    return hasil

def input_judul() -> str:
    while True:
        judul = input('Judul\t\t: ')
        if len(judul) <= 255:
            break
        else:
            print('Judul tidak boleh lebih dari 255 karakter.')
    return judul

def input_publisher() -> str:
    while True:
        publisher = input('Publisher\t: ')
        if len(publisher) <= 255:
            break
        else:
            print('Nama publisher tidak boleh lebih dari 255 karakter.')
    return publisher

def input_tahun() -> int:
    while True:
        try:
            tahun: int = int(input('Tahun\t\t: '))
            if len(str(tahun)) <= 4 and tahun > 0:
                break
            else:
                print('Tahun tidak valid, silakan masukkan kembali.')
        except:
            print('Tahun tidak valid, silakan masukkan kembali.')
    return tahun
