while True:
    day = 1
    km_start = int(input('Количество км (начало):'))
    km_result = int(input('Количество км (результат):'))
    if km_start > km_result:
        print('Введены неверные данные!')
    else:
        while km_start < km_result:
            km_start += km_start * 0.1
            day += 1
        print('Ответ: на {} день спортсмен достиг результата'.format(day))
        break

