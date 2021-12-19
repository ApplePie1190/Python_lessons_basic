numbers_a = [number ** 3 for number in range(1000) if number % 2 > 0]
numbers_b = [number + 17 for number in numbers_a if number]


def sum_list(numbers):
    total = 0
    for number in numbers:
        result = 0
        number_for_sum = number
        while number:
            result += number % 10
            number //= 10
        if result % 7 == 0:
            total += number_for_sum
    return total


def sum_list17(numbers):
    total = 0
    for number in numbers:
        result = 0
        number_tasc_c = number + 17
        number_for_sum = number_tasc_c
        while number_tasc_c:
            result += number_tasc_c % 10
            number_tasc_c //= 10
        if result % 7 == 0:
            total += number_for_sum
    return total


print('список задание А: ', numbers_a)
print('список задание Б: ', numbers_b)
print('сумма задание А: ', sum_list(numbers_a))
print('сумма задание Б: ', sum_list(numbers_b))
print('сумма задание С: ', sum_list17(numbers_a))
