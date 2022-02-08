numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
with open('Ex4Less5.txt') as file, open('new_file.txt', 'w') as n_f:
    f_l = file.readlines()
for line in f_l:
    number_info = line.split('-')
    rus_number = numbers.get(number_info[0])
    new_file.write(f'{line.replase(number_info[0], rus_number)}')
