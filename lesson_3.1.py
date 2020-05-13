a = float(input('Введите число: '))
b = float(input('Введите число: '))

def exe_1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No value'

def exe_1_use():
    print(exe_1(int(input('Введите число: '))),
               (int(input('Введите число: '))))
