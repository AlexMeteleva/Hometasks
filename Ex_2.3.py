user_month=int(input('Введите число: '))
month_list=['', 'зима', 'зима', 'весна','весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
month_dict={ 1: 'зима',
             2: 'зима',
             3: 'весна',
             4: 'весна',
             5: 'весна',
             6: 'лето',
             7: 'лето',
             8: 'лето',
             9: 'осень',
             10: 'осень',
             11: 'осень',
             12: 'зима'
             }
print(month_list[user_month])
print(month_dict[user_month])
