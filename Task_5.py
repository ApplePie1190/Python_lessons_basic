src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_num = set()
tmp = set()
for num in src:
    if num not in tmp:
        unique_num.add(num)
    else:
        unique_num.discard(num)
    tmp.add(num)

result = [num for num in src if num in unique_num]
print(result)
