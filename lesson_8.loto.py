# Карточка должна состоять из 3 строк и 9 столбцов:
#
# Цифры в столбцах:
# 1 - от 1 до 9
# 2 - от 10 до 19
# 3 - от 20 до 29
# 4 - от 30 до 39
# 5 - от 40 до 49
# 6 - от 50 до 59
# 7 - от 60 до 69
# 8 - от 70 до 79
# 9 - от 80 до 90 !!!
#
# Количество рандомных не повторяющихся чисел в карточке - 15
#
#
#

import random
import sys

ballsleft = 90

card_1 = 15
card_2 = 15
balls = random.sample(range(90), 90)
game_set = random.sample(range(90), 30)
card_1_set = random.sample(game_set, 15)
card_2_set = [e for e in game_set if not e in card_1_set]
card_1_field = [card_1_set[:5], card_1_set[5:10], card_1_set[10:]]
card_2_field = [card_2_set[:5], card_2_set[5:10], card_2_set[10:]]


for card_1line in card_1_field:
    card_1line.sort()
    card_1line.insert(random.randint(1, 4), ' ')
    card_1line.insert(random.randint(1, 5), ' ')
    card_1line.insert(random.randint(1, 6), ' ')
    card_1line.insert(random.randint(1, 7), ' ')

for card_2line in card_2_field:
    card_2line.sort()
    card_2line.insert(random.randint(1, 4), ' ')
    card_2line.insert(random.randint(1, 5), ' ')
    card_2line.insert(random.randint(1, 6), ' ')
    card_2line.insert(random.randint(1, 7), ' ')


def field(p):
    if p == 0:
        print('{:-^26}'.format('Ваша карточка'))
        for line1 in card_1_field:
            for n1 in line1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if p == 1:
        print('{:-^26}'.format('Карточка компьютера'))
        for line2 in card_2_field:
            for n2 in line2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))

# Процесс игры

def you_move():
    a = input('Зачеркнуть цифру? (y/n): ')
    if a == 'y':
        if ball in card_1_set:
            for l in card_1_field:
                try:
                    l.insert(l.index(ball), 'x')
                    l.pop(l.index(ball))
                except ValueError:
                    continue
            print('\nOK')
            return 1
        else:
            print('\nТЫ ВЫИГРАЛ!  GAME OVER')
            sys.exit()
    if a == 'n':
        if ball in card_1_set:
            print('\nТЫ ВЫИГРАЛ!  GAME OVER')
            sys.exit()
        else:
            print('\nOK')


def com_move():
    if ball in card_2_set:
        for i in card_2_field:
            try:
                i.insert(i.index(ball), 'x')
                i.pop(i.index(ball))
            except ValueError:
                continue
        return 1


for ball in balls:
    ballsleft -= 1
    print('\nНовый бочонок: {} (осталось: {})\n'.format(ball, ballsleft))
    field(0)
    field(1)
    if you_move() == 1:
        card_1 -= 1
    if com_move() == 1:
        card_2 -= 1
    if card_1 == 0:
        print('\nТЫ ВЫИГРАЛ!')
        sys.exit()
    if card_2 == 0:
        print('\nТЫ ПРОИГРАЛ!')
        sys.exit()
    if ballsleft == 0:
        print('\nТЫ ВЫИГРАЛ!  GAME OVER')
        sys.exit()
