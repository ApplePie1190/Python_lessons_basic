class MyOwnErr(Exception):
    pass


user_number = int(input('введите делитель: '))

try:
    if user_number == 0:
        raise MyOwnErr('делитель не может равняться нулю')
except (ValueError, MyOwnErr) as err:
    print(err)
else:
    print(f'делитель {user_number} введен корректно')
