from fanctools import reduce

def mul_func(prev_el, el):
    return prev_el * el

my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(mul_func, my_list))