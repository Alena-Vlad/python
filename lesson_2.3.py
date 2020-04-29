month = int(input('Введите номер месяца:'))
if month > 12:
    print('Номер месяца введен не верно!')

month_list = dict()
month_list = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

for key in month_list.keys():
    if month in month_list[key]:
        print(key)


