class MyOwnErr(Exception):
    pass


numbers = []
while True:
    user_number = input('введите число чтобы добавить в список, чтобы закончить введите stop: ')
    try:
        if user_number.isdigit():
            numbers.append(int(user_number))
        elif user_number == 'stop':
            break
        else:
            raise MyOwnErr('это не число')
    except MyOwnErr as err:
        print(err)
print(numbers)
