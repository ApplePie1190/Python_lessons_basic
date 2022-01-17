import sys

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.writelines(sys.argv[1])
    f.writelines('\n')