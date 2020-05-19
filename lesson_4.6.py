# 1
from intertool import count, cycle

for i in count(int(input('Введите число: ')))
    print(i)



# 2
my_list = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 8, 3, 5, 12, 8, 9]

iter = cycle(my_list)
stop = ''
while stop != 'q':
    print(next(iter), end='')
    stop = input()