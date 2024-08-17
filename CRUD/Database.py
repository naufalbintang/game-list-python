from . import Operasi

DB_NAME: str = 'data.txt'
TEMPLATE: dict[str, str] = {
    'pk': 'xxxxxx',
    'date_add': 'dd-mm-yyyy',
    'judul': ' ' * 255,
    'publisher': ' ' * 255,
    'tahun': 'yyyy'
}


def init_console() -> str:
    try:
        with open(DB_NAME, 'r') as file:
            print('Database tersedia, init done.')
    except:
        print('Database tidak ditemukan, silakan buat database baru.')
        Operasi.create_first_data()
        