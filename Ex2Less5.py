with open ('Ex2Less5.txt', 'r') as file_r:
    file_r = file_r.readlines()
    count=0
    for el, line in enumerate(file_r):
        count +=1
        words = len(line.split())
        print(f'Количество слов в строке {el+1}: {words}')
    print(f'Количество строк в файле: {count}')
