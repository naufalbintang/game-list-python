from . import Database, Input, Util
import datetime

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
    
    data_str = f'{template_copy['pk']},{template_copy['date_add']},{template_copy['judul']},{template_copy['publisher']},{template_copy['tahun']}'
    
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('Gagal membuat database.')
    