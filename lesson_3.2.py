name = input('Введите имя: ')
suname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
town = input('Введите город проживания: ')
email = input('Введите email: ')
tel = input('Введите номер телефона: ')

def exe_2(**kwargs):
    return list(kwargs.values())


def exe_2_use():
    print(exe_2(name=input('Введите имя: '),
                suname=input('Введите фамилию: '),
                year=input('Введите год рождения: '),
                town=input('Введите город проживания: '),
                email=input('Введите email: '),
                tel=input('Введите номер телефона: ')))