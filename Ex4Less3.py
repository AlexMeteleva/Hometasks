def my_func(x, y):
    result = x ** y
    return result
def my_func_2(x, y):
    count = 1
    for i in range (y * -1):
        count *= x
        result = x
    return 1/ count
num_1 = int(input('Введите число x: '))
num_2 = int(input('Введите число y: '))
print(my_func(num_1, num_2))
print(my_func_2(num_1, num_2))
