#!/usr/bin/env python3.7
import PyPDF2
from time import sleep

fi = str(input('Digite o caminho absoluto para o pdf encryptado: ')).strip()

dic = open('dictionary.txt')
l = dic.readlines()

o = PyPDF2.PdfFileReader(open(fi,'rb'))

count = 1
print('AGUARDE!!!')
for w in l:
    w = w.strip()
    low = w.lower()
    up = w.upper()
    count += 1
    print('_', end='',flush=True)
    sleep(0.01)
    if o.decrypt(low) == 1:
        print('OK!!!')
        print(f'\nessa é a senha --> {low}')
        break
    elif o.decrypt(up) == 1:
        print('OK!!!')
        print(f'\nEssa é a senha --> {up}')
        break
print(f'Com {count-1} tentativas')

