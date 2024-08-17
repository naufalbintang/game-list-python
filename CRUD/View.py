from . import Operasi, Input

def update_data():
    read_data()
    while True:
        print('Silakan pilih nomor game yang akan diupdate')
        no_game = Input.input_no_game()
        data_game = Operasi.read(index=no_game)
        
        if data_game:
            break
        else:
            print('Nomor tidak valid, silakan masukkan lagi.')
    
    data_break = data_game.split(',')
    pk = data_break[0]
    date_add = data_break[1]
    judul = data_break[2]
    publisher = data_break[3]
    tahun = data_break[4][:-1]
    
    # print(data_break)
    # print(pk)
    # print(date_add)
    # print(judul)
    # print(publisher)
    # print(tahun)
    
    while True:        
        print('\n' + '=' * 100)
        print('Silakan pilih data yang ingin diupdate')
        print(f'1. Judul\t: {judul:.40}')        
        print(f'2. Publisher\t: {publisher:.40}')
        print(f'3. Tahun\t: {tahun:4}')
        
        pilihan_user = Input.pilihan_user(1, 3)
        
        match pilihan_user:
            case 1: judul = Input.input_judul()
            case 2: publisher = Input.input_publisher()
            case 3: tahun = Input.input_tahun()
        
        print('\nBerikut adalah data yang baru')
        print(f'1. Judul\t: {judul:.40}')        
        print(f'2. Publisher\t: {publisher:.40}')
        print(f'3. Tahun\t: {tahun:4}')

            
        is_done = input('Apakah data sudah sesuai (y/N)? ')
        if is_done.lower() == 'n' or is_done == '':
            pass
        elif is_done.lower() == 'y':
            break
        else:
            print('Input tidak valid, silakan coba lagi.')
    
    Operasi.update(no_game, pk, date_add, judul, publisher, tahun)
    
        
        

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