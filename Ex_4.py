user_number = int(input('Введите число: '))
max_digit = 0
while user_number != 0:
    last_digit = user_number % 10
    if last_digit > max_digit:
        max_digit = last_digit
    user_number = user_number // 10
print(max_digit)
