text = input('Введите строку из нескольких слов: ')
list = text.split()
for i in text.split():
    if (len(i) > 10):
        print(text[:10])
        continue
    print(i)



