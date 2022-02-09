lesson = {}
with open('Ex6Less5.txt') as file:
    file_l=file.readlines()
for line in file_l:
    lesson_inf = line.split()
    hours = 0
    for i in lesson_inf [1:]:
        if i != '-':
            num = 0
            for el in i:
                if el.isdigit():
                    num += 1
                else:
                    break
            hours += int(num)
    lesson.update({lesson_inf[0].strip(':'): hours})
print(lesson)
