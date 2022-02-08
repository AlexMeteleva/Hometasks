import random
with open('file_num.txt', 'w') as file:
    for i in range(15):
        file.write(f'{random.randint(0, 10)}')
with open('file_num.txt') as file:
    string = file.read().split()
    amount = 0
    for n in string:
        amount += int(n)
print(amount)
