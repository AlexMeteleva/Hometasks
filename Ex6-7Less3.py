def str_func(txt):
    word = txt[0].upper() + txt[1:].lower()
    return word
string = input('Введите строку: ')
for word in string.split(' '):
    print(f'{str_func(word)}', end=' ')
