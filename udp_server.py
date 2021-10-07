#!/usr/bin/env python3
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('0.0.0.0', 8088))

print('Wait for connecting...')

while True:
    # 接收数据:
    conn, addr = s.recvfrom(1024)
    str1 = conn.decode('utf-8')
    print('I received a string is: ',str1)
    str2 = str1.upper()
    s.sendto(str2.encode('utf-8'), addr)
    if str1 == '.':
        break
s.close()
