#!/usr/bin/env python3

import PyPDF2
pdf = open('ty.pdf', 'rb')


reader = PyPDF2.PdfFileReader(pdf)
writer = PyPDF2.PdfFileWriter()

quant = reader.numPages

print(f"Possui {quant} páginas")

q = int(input('Qual página?: '))
page = reader.getPage(q)
writer.addPage(page)

out = open('um.pdf','wb')
writer.write(out)
out.close()
pdf.close()
