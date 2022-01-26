user_str=input('Введите несколько слов: ')
list_str = user_str.split(' ')
for ind, el in enumerate(list_str, 1):
    print(ind, el [:10])
