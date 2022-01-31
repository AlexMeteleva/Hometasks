def user_info (name, surname, years_bd, city, email, phone_number) :
    return f'{name} {surname} {years_bd} года рождения из города {city}, e-mail - {email}, номер телефона - {phone_number}'

user_name = input('Введите Ваше имя: ')
user_surname = input('Введите Вашу фамилию: ')
user_years_bd = input('Введите год Вашего рождения: ')
user_city = input('Введите город Вашего проживания: ')
user_email = input('Введите Ваш e-mail: ')
user_phone_number = input('Введите Ваш номер телефона: ')
print(user_info(name= user_name, surname=User_surname, years_bd=user_years_bd, city=user_city, email=user_email, phone_number=user_phone_number))
