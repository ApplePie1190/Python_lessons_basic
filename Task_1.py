result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        el = line.split()
        result.append((el[0], el[5][1:], el[6]))
print(result)

