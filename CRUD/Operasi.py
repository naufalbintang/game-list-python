from . import Database, Input, Util
import datetime

def create():
    judul = Input.input_judul()
    publisher = Input.input_publisher()
    tahun = Input.input_tahun()
    
    template_copy = Database.TEMPLATE.copy()
    template_copy['pk'] = Util.random_str(6)
    template_copy['date_add'] = datetime.datetime.now().replace(microsecond=0)
    template_copy['judul'] = judul + ' ' * (255 - len(judul))
    template_copy['publisher'] = publisher + ' ' * (255 - len(publisher))
    template_copy['tahun'] = tahun
    
    data_str = f'{template_copy['pk']},{template_copy['date_add']},{template_copy['judul']},{template_copy['publisher']},{template_copy['tahun']}\n'
    
    try:
        with open(Database.DB_NAME, 'a',encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('Gagal menambahkan data.')
    
    

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            banyak_game = len(content)
            if 'index' in kwargs:
                index_game = kwargs['index'] - 1
                if index_game < 0 or index_game > banyak_game:
                    return False
                else:
                    return content[index_game]
            else:
                return content
    except:
        print('Gagal membaca database.')
        return False

def create_first_data():
    judul = Input.input_judul()
    publisher = Input.input_publisher()
    tahun = Input.input_tahun()
    
    template_copy = Database.TEMPLATE.copy()
    template_copy['pk'] = Util.random_str(6)
    template_copy['date_add'] = datetime.datetime.now().replace(microsecond=0)
    template_copy['judul'] = judul + ' ' * (255 - len(judul))
    template_copy['publisher'] = publisher + ' ' * (255 - len(judul))
    template_copy['tahun'] = str(tahun)
    
    data_str = f'{template_copy['pk']},{template_copy['date_add']},{template_copy['judul']},{template_copy['publisher']},{template_copy['tahun']}\n'
    
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('Gagal membuat database.')
    