def exe_6(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)


def exe_6_use():
    print(exe_6(input('Input text: ').split()))


def sep():
    print('+' * 30)




