import os

root_dir = './'
size_stat = {}
for root, dirs, files in os.walk(root_dir):  # получаем все вложенные дирректории корневой папки
    for file in os.scandir(root):  # проходим по вложеным директориям
        if file.is_file():  # ищем файлы
            stat_size = 10  # задаем минимальный размер
            file_size = file.stat().st_size  # запоминаем размер файла
            if file_size < stat_size:  # если размер файла меньше минимально заданого, то он он идет в ключ 0 словаря
                key = 0
            else:
                while file_size > stat_size:  # если он больше то определяем в какую категорию размеров он идет
                    stat_size *= 10
                key = stat_size
            if key in size_stat.keys():  # заполняем словарь
                size_stat[key] += 1
            else:
                size_stat.setdefault(key, 1)
print(size_stat)
