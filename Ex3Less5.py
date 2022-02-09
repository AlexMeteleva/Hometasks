with open('Ex3Less5.txt') as file:
    file_l=file.readlines()
staff = {}
amount = 0
for line in file_l:
    staff_inf = line.split()
    staff.update({staff_inf[0]: float (staff_inf[1])})
    amount += float (staff_inf[1])
aver_amount = round(amount/len(staff), 2)
print(f'средняя заработная плата составляет: {aver_amount}')
for key, val in staff.items():
    if val < 20000:
        print(f' {key}: {val}')

