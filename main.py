import os
import CRUD.Input as Input
import CRUD

if __name__ == '__main__':
    sistem_operasi = os.name
    match sistem_operasi:
        case 'nt': os.system('cls')
        case 'posix': os.system('clear')
    
    # check database
    CRUD.init_console()
    input('pause (main.py)')
    
    while True:
        match sistem_operasi:
            case 'nt': os.system('cls')
            case 'posix': os.system('clear')
            
        print('\nSELAMAT DATANG')
        print('DI PROGRAM LIST GAME')
        print('=' * len('DI PROGRAM LIST GAME') + '\n')
        
        list_pilihan: list[str] = ['Keluar', 'Read Data', 'Create Data', 'Update Data', 'Delete Data']
        banyak_pilihan: int = len(list_pilihan)
        for nomor, pilihan in enumerate(list_pilihan):
            print(f'{nomor}. {pilihan}')
        
        pilihan_user: int = Input.pilihan_user(banyak_pilihan)
        
        match pilihan_user:
            case 0: break
            case 1: CRUD.read_data()
            case 2: print('Create Data') 
            case 3: print('Update Data') 
            case 4: print('Delete Data') 
            
        is_done: str = input('\nApakah ingin keluar (y/N)? ')
        if is_done.lower() == 'n' or is_done == '':
            pass
        elif is_done.lower() == 'y':
            break
        else:
            print('Input tidak valid.')
            break
        
    print('Program selesai.')
        