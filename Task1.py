duration = int(input('Введите временной интервал: '))
day = duration // 86400
hour = (duration - day * 86400) // 3600
minute = (duration - day * 86400 - hour * 3600) // 60
second = duration % 60
time = [day, 'дн', hour, 'час', minute, 'мин', second, 'сек']
for i in range(0, len(time)-1, 2):
    if time[i]:
        print(time[i], time[i + 1], end=' ')
