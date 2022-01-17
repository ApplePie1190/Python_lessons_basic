import json
import sys

with open('users.csv', 'r', encoding='utf-8') as f:
    names = [line.replace(',', ' ').replace('\n', '') for line in f]

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobbys = [line.replace(',', ', ').replace('\n', '') for line in f]

if len(names) < len(hobbys):
    sys.exit(1)
else:
    data = {names[i]: hobbys[i] if i < len(hobbys) else None for i in range(len(names))}

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

    with open('result.json', 'r', encoding='utf-8') as f:
        file_data = json.load(f)

    print(file_data)
