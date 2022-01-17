import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        print(f.read())
    elif len(sys.argv) == 2:
        prices = f.readlines()
        for i in range(int(sys.argv[1]) - 1,len(prices)):
            print(prices[i].replace('\n', ''))
    elif len(sys.argv) == 3:
        prices = f.readlines()
        for i in range(int(sys.argv[1]) - 1, int(sys.argv[2])):
            print(prices[i].replace('\n', ''))



