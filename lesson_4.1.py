# 1
import sys

hours, salary_per_hour, bonus = map(float, sys.argv[1:])
print('salary - {}'.format(hours * salary_per_hour + bonus))


# 2
def simple_calc():
    hours = float(input('Введите количество отработанных часов: '))
    salary_per_hour = float(input('Введите ставку оплаты труда за 1 час: '))
    bonus = float(input('Укажите сумму премии: '))
    pay = hours * salary_per_hour
    return pay + bonus

print(f'Размер заработной платы составил: {simple_calc()}')