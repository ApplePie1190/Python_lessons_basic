import re

pattern1 = re.compile(r'^([^\s]+)\s+')
pattern2 = re.compile(r'\[([^\[\]]+)]')
pattern3 = re.compile(r'"([A-Z]+)\s')
pattern4 = re.compile(r'\s([/][a-z0-9_/]+)\s')
pattern5 = re.compile(r'"\s(\d+)')
pattern6 = re.compile(r'(\d+)\s"')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = pattern1.findall(line)
        request_datetime = pattern2.findall(line)
        request_type = pattern3.findall(line)
        requested_resource = pattern4.findall(line)
        response_code = pattern5.findall(line)
        response_size = pattern6.findall(line)
        result = (remote_addr[0],
                  request_datetime[0],
                  request_type[0],
                  requested_resource[0],
                  response_code[0],
                  response_size[0])
        print(result)
