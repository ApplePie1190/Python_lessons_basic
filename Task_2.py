import re

pattern = re.compile(r'^([^\s]+)[-\s\[]+([^\[\]]+)[\s"\]]+([A-Z]+)\s([/][a-z0-9_/]+)[\sA-Z1/\."]+(\d+)\s(\d+)\s"')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        result = pattern.findall(line)[0]
        print(result)
