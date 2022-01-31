def div_nums (num_1, num_2) :
    if num_2 != 0:
        return num_1 / num_2
    else:
        return 'Деление на ноль запрещено!'

num_1 = float(input('Введите число 1: '))
num_2 = float(input('Введите число 2: '))
print(div_nums(num_1, num_2))
