my_dict = dict()
with open('5.6.txt') as f:
    lines = f.readlines()
    for line in lines:
        splitted_line = line.split()
        subject = splitted_line[0]
        sum_lessons = sum([int(x[:x.find(' (')]) for x in splitted_line[1:] if '(' in x])
        my_dict[subject] = sum_lessons
    print(my_dict)
