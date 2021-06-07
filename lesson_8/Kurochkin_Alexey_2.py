# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
#
# ля получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)

import re

with open('nginx_logs.txt', 'r') as logs_nginx:
    pattern_ip = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s[-]'

    for line in logs_nginx:
        remote_addr = re.findall(pattern_ip, line)

        print(remote_addr)
        break
