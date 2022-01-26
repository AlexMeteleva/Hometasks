num = int(input('Введите количество элементов в списке: '))
my_list = []
for i in range(num):
    elem = input('Введите элемент списка: ')
    my_list.append(elem)

if num > 1:
    i = 0
    while i < num - 1:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        i += 2
print(my_list)
