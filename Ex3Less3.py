def my_func(num_1, num_2, num_3):
    sum_nums = num_1 + num_2 + num_3
    return sum_nums - min(num_1, num_2, num_3)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
result = my_func(a, b, c)
print(result)
