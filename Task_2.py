def num_translate_adv(number):
    translate_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if number.istitle():
        print(translate_dict.get(number.lower()).title())
    else:
        print(translate_dict.get(number))


user_number = input('введите число для перевода: ')
num_translate_adv(user_number)
