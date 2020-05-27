from math import factorial
from itertools import count

def fibo_gen():
    for el in count(1):
        yield factorial(el)

x = 0
for i in fibo_gen():
    print('Factorial {} - {}'.format(x + 1, i))
    if x == 14:
        break
    x +=1