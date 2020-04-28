numb_1 = int(input('Введите целое положительное число:'))
numb_max = 0
numb = numb_1
while numb > 0:
    digit = numb % 10
    if digit > numb_max:
        numb_max = digit
        if numb_max == 9:
            break
    numb = numb//10
 print('Наибольшая цифра у введенного числа:', numb_max)
