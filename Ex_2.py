user_seconds = int(input('Введите количество секунд '))
seconds = user_seconds % 60
minutes = (user_seconds // 60) % 60
hours = user_seconds // 3600
result = f'{hours:02}:{minutes:02}:{seconds:02}'
print(result)
