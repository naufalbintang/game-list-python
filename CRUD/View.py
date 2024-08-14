from . import Operasi

def create_data():
    print('\n' + '=' * (len('silakan buat data baru') + 1))
    print('Silakan buat data baru')
    Operasi.create()
    print('\nBerikut data baru anda')
    read_data()

def read_data():
    data_file = Operasi.read()
    index = 'No'
    judul = 'Judul'
    publisher = 'Publisher'
    tahun = 'Tahun'
    
    # header
    print('\n' + '=' * 100)
    print(f' {index:4} | {judul:40} | {publisher:40} | {tahun:5}')
    print('-' * 100)
    
    # data
    for index, data in enumerate(data_file, 1):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        judul = data_break[2]
        publisher = data_break[3]
        tahun = data_break[4]
        print(f' {index:<4} | {judul:.40} | {publisher:.40} | {tahun:5}', end='')
        
    # footer
    print('=' * 100)