revenue = float(input('Введите суммы выручки фирмы, тыс. руб.: '))
costs = float(input('Введите сумму издержек фирмы, тыс. руб.: '))
prof = ((revenue - costs) / revenue)*100
emplo = int(input('Численность сотрудников фирмы, чел.: '))
profit = revenue - costs
profit_emplo = profit / emplo

if revenue > costs:
    print('Прибыль, рыс. руб.: ', profit)
    print('Рентабельность, %: ', prof)

if revenue > costs and emplo > 0:
    print('Прибыль фирмы в расчете на одного сотрудника, тыс. руб. /чел.: ', profit_emplo)
if revenue < costs:
    print('Убыток, тыс. руб.: ', profit)


