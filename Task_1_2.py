def odd_nums(n):
    for nums in range(1, n + 1, 2):
        yield nums  # создаем генератор нечетных чисел от 1 до n


odd_nums_15 = odd_nums(15)
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))


def odd_nums_adv(n):
    nums = []
    for num in range(1, n + 1, 2):
        nums.append(num)
    return nums  # генерируем список нечетных чисел от 1 до n


print(odd_nums_adv(15))
