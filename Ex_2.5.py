my_list = [7, 5, 3, 3, 2]
new_elem=int(input('Введите число: '))
flag = False
for index, el in enumerate(my_list):
    if new_elem > el:
        my_list.insert(index, new_elem)
        flag = True
        break
if not flag:
    my_list.append(new_elem)
print (my_list)