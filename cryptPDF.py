#!/usr/bin/env python3.7

import PyPDF2
from time import sleep
from getpass import getpass

op = str(input('Digite o nome do arquivo PDF: ')).strip()
key = getpass('Digite sua Senha: ')
fil = str(input('Digite o nome da saída do PDF Encriptado: ')).strip()
pdfFile = open(op,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

print('Encriptando Aguarde...')
for pageNum in range(pdfReader.numPages):
    print('#',end='',flush=True)
    sleep(0.03)
    pdfWriter.addPage(pdfReader.getPage(pageNum))
print('Finalizando!')

pdfWriter.encrypt(key)
resultPdf = open(f'{fil}.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()

#for i in range(6):
#    sleep(1.5)
#    print('.',end = '', flush=True)
print('\nEncrypted!!!')
