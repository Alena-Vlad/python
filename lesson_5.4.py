with open('12345.txt', encoding='utf-8') as f:
    lines = f.readlines()

with open('rus.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        if '2' in line:
            line = line.replace('Two', 'Два')
        if '3' in line:
            line = line.replace('Three', 'Три')
        if '4' in line:
            line = line.replace('Four', 'Четыре')
        f.write(line)
