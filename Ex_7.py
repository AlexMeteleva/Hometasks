start_km = int(input('Начальное расстояние бега составляет: '))
finish_km = int(input('Целевое расстояние бега составляет: '))
count = 1
while start_km <= finish_km:
    start_km = (start_km * 110) / 100
    count += 1
print(f'На {count} день спортсмен достиг результата — не менее {finish_km} км')
