def price_list(incoming_list):  # функция вывода списка в формате <r> руб <kk> коп
    for price in incoming_list:
        rubles = int(price)
        kopecks = round((price - rubles) * 100)
        print(f"{int(price)} руб {kopecks:02d} коп", end=', ')
    print('\n')


my_list = [57.8, 46.51, 97, 123.07, 5.56, 46, 15.72, 27.05, 34, 46.89]
price_list(my_list)  # вывода списка в формате <r> руб <kk> коп
my_list.sort()
print(my_list)  # вывод отсортированого по возрастанию списка
new_list = my_list.copy()
new_list.reverse()
print(new_list)  # вывод нового списка отсортированого по убыванию
for i in range(5):
    print(new_list[i])  # вывод 5 самых дорогих цен
