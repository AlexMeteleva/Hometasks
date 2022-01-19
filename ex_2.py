user_seconds = int(input('Введите количество секунд: '))
number_of_seconds = user_seconds % 60
number_of_minutes = (user_seconds // 60) % 60
number_of_hours = user_seconds // 3600
result = f'{number_of_hours:02}:{number_of_minutes:02}:{number_of_seconds:02}'
print(result)
