import os


def create_file_or_folder(name):
    if '.' in name:
        with open(name, 'a', encoding='utf-8') as file:
            file.write('')
    elif not os.path.exists(name):
        os.makedirs(name)


dir_lvl = 0
with open('config.yaml', 'r', encoding='utf-8') as f:
    for line in f:
        temp_dir_lvl = line.rindex('|--')  # запомнили уровень файла или папки
        file_folder_name = line.replace('\n', '').split('|--')[-1]  # получили имя файла или папки из строки файла
        if temp_dir_lvl == dir_lvl:  # уровень не изменился
            create_file_or_folder(file_folder_name)  # создали файл или папку
            if '.' not in file_folder_name:  # если папка, то запомнили имя папки
                temp_name = file_folder_name
        elif temp_dir_lvl > dir_lvl:  # уровень изменил
            os.chdir(temp_name)  # зашли в сохраненную папку
            create_file_or_folder(file_folder_name)  # создали файл или папку
            dir_lvl = temp_dir_lvl  # запомнили уровень
            if '.' not in file_folder_name:  # если папка, то запомнили имя папки
                temp_name = file_folder_name
        else:
            for i in range(0, dir_lvl - temp_dir_lvl, 3):
                directory = os.path.split(os.getcwd())  # нужное кол-во раз вернулись на папку выше
                os.chdir(directory[0])
            create_file_or_folder(file_folder_name)  # создали файл или папку
            dir_lvl = temp_dir_lvl  # запомнили уровень
            if '.' not in file_folder_name:  # если папка, то запомнили имя папки
                temp_name = file_folder_name
