TEMPLATE = {
    'pk': 'xxxxxx',
    'date_add': 'dd-mm-yyyy',
    'judul': ' ' * 255,
    'pubsliher': ' ' * 255,
    'tahun': 'yyyy'
}

template_copy = TEMPLATE.copy()
judul = input('Judul: ')
template_copy['judul'] = judul + ' ' * (255 - len(judul))
print(len(template_copy['judul']))

judul = input('Judul: ')
template_copy['judul'] = judul + ' ' * (255 - len(judul))
print(len(template_copy['judul']))

