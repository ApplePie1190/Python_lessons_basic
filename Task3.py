word_end1 = [1]
word_end2 = [[5, 6, 7, 8, 9, 0], [11, 12, 13, 14]]

for i in range(1, 101):
    if (i % 10 in word_end1 and i not in word_end2[1]) or i in word_end1:
        print(i, 'процент')
    elif i % 10 in word_end2[0] or i in word_end2[0] or i in word_end2[1]:
        print(i, 'процентов')
    else:
        print(i, 'процента')
