user_revenue = int(input("Каков размер выручки? "))
user_cost = int(input('Каков размер издержек? '))
if user_revenue > user_cost:
    print('Вы работаете с прибылью!')
    profit = user_revenue - user_cost
    print(f'Ваша выручка составила {profit}')
    employes = int(input('Введите количество сотрудников в компании: '))
    profit_per_employee = profit / employes
    print(f'Прибыль фирмы в расчёте на одного сотрудника составляет {profit_per_employee} ')
else:
    print('Вы работаете в убыток!')
