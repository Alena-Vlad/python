def exe_5():
    res = 0
    while True:
        numbers = input('Enter list of number or * to exit: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Sum is {res}. Exit')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Enter number or *')
        print(f'Sum is {res}')