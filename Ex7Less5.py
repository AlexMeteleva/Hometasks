import json
companies = {}
count = 0
summ = 0
with open('Ex7Less5.txt') as file:
    f_l=file.readlines()
    for line in f_l:
        inform = line.split()
        profit = float(inform[2]) - float(inform[3])
        companies.update({inform[0]: profit})
        if profit >0:
            count +=1
            summ += profit
aver_prof = summ / count
result = [companies, {'aver_prof' : aver_prof}]
with open ('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file)
with open ('result.json', 'w', encoding='utf-8') as file:
    result = json.load(file)
    print(result)
