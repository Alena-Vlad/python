with open("12345.txt", "w") as f:
    while True:
        line = input('Введите строку: ')
        if line == '':
            break
        f.write(line + '\n')

