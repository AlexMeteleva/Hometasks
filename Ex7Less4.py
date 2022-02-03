def gen_fact(num):
    amp = 1
    for i in range(1, num + 1):
        amp *= i
        yield amp

amount = int(input('Факториал какого числа нужно найти: '))
for elem in gen_fact(amount):
    print(elem)
