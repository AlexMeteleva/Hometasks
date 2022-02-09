with open ("Ex1Less5.txt", "w") as f_j:
    str = input ('Что необходимо записать в новый файл? \n')
    while len(str) != 0:
        f_j.write (f'{str}\n')
        str = input ('Что необходимо записать в новый файл? \n')

