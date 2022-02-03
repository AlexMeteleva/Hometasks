from itertools import count, cycle
start = int(input('С какого числа мне начать: '))
stop = int(input('А каким закончить: '))
for i in count (start):
    if i > stop:
        break
    else:
        print(i)
amount=0
items=['Шоколад', 'Тунец', 'Хлопья', 'Есентуки']
for item in cycle(items):
    if amount > 15:
        break
    print(item)
    amount +=1
