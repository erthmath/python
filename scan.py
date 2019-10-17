#!/usr/bin/env python3.7


import socket


ip = input('Enter IP: ')
port = int(input('Enter PORT: '))

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

if s.connect_ex((ip , port)):
    print(f'Porta {port}, is closed')
else:
    print(f'Porta {port} está aberta')






