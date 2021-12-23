my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in reversed(range(len(my_list))):
    if my_list[i].isdigit():  # проверка элемента списка на числовой элемент
        my_list[i] = f'{int(my_list[i]):02d}'  # форматирование числа
        my_list.insert(i, '"')  # добавляем ковычки до
        my_list.insert(i + 2, '"')  # добавляем ковычки после
    else:
        for j in range(len(my_list[i])):
            if my_list[i][j].isdigit():  # проверка элементов посимвольно если явно не выявлено число
                my_list[i] = my_list[i][:j] + f'{int(my_list[i][j:]):02d}'  # форматирование числа
                my_list.insert(i, '"')  # добавляем ковычки до
                my_list.insert(i + 2, '"')  # добавляем ковычки после
                break

print(my_list)

final_msg = ''
i = 0
while i < len(my_list):  # формирование строки
    if my_list[i] == '"':
        final_msg += f'{my_list[i]}{my_list[i + 1]}{my_list[i + 2]} '
        i += 3
    else:
        final_msg += f'{my_list[i]} '
        i += 1

print(final_msg)
