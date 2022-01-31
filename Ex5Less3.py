def sum_nums (num_str, stop):
    nums_list = num_str.split(' ')
    sum_list = 0
    for i in nums_list:
        if i == stop:
            break
        sum_list += int(i)
    return sum_list
stopper = "?"
finished = False
sum_str = 0
while not finished:
    user_nums_str = input('Введите строку чисел через пробел: ')
    sum_str += sum_nums(user_nums_str, stopper)
    finished = stopper in user_nums_str
    print(f'Сумма равна {sum_str}')
