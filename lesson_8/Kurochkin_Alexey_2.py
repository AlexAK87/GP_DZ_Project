import re

with open('nginx_logs.txt', 'r') as logs_nginx:
    pattern_ip = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3} |[a-z0-9:]+:[a-z0-9:]+:[a-z0-9:]+:[a-z0-9:]+:[a-z0-9:]+:[' \
                 r'a-z0-9:]+|[a-z0-9:]+:[a-z0-9:]+ '
    pattern_datetime = r'\d{2}/[a-zA-z]+/\d{4}:\d{2}:\d{2}:\d{2}\W[0-9+]{0,5}'
    pattern_type = r'[A-Z]+ '
    pattern_resource = r'/[a-z]+/[a-z0-9_]+'
    pattern_code = r' [0-9]+'
    pattern_size = r' \w+'

# Особенные строки добавил шаблон через |(or)
# 2001:4801:7824:102:8bee:6e66:ff10:6aa2
# 2a01:7e00::f03c:91ff:fe70:a4cc
# 2a01:4f8:201:84d6::2
    for raw in logs_nginx:
        parsed_raw_list = []
        remote_addr = re.search(pattern_ip, raw)
        request_datetime = re.findall(pattern_datetime, raw)
        request_type = re.findall(pattern_type, raw)
        requested_resource = re.findall(pattern_resource, raw)
        response_code = re.findall(pattern_code, raw)
        response_size = re.findall(pattern_size, raw)

        parsed_raw_list.append(remote_addr[0].replace(' ', ''))
        parsed_raw_list.append(request_datetime[0])
        parsed_raw_list.append(request_type[0].replace(' ', ''))
        parsed_raw_list.append(requested_resource[0])
        parsed_raw_list.append(str(response_code[0]).replace(' ', ''))
        parsed_raw_list.append(response_size[2].replace(' ', ''))

        print(tuple(parsed_raw_list))
