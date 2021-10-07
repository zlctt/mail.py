#!/usr/bin/env python3
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(('127.0.0.1',8088))

print('I am connecting the server!')
for data in ['aBch','f 服务 d','h7Tq','.']:
    # 发送数据:
    s.sendto(data.encode('utf-8'), ('127.0.0.1',8088))
    
    str1 = s.recv(1024).decode('utf-8')
    # 接收数据:
    print('The original string is: ',data,'\tthe processed string s: ',str1)

s.close()
