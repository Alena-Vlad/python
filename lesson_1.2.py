numb_sec = int(input('Веедите время в секундах'))
numb_hour = numb_sec // 360
numb_hour_1 = numb_sec % 360
numb_min = numb_hour_1 // 60
numb_sec_1 = numb_hour_1 % 60
print(f' {numb_hour:02}: {numb_min:02} :{numb_sec_1:02}')


