#!/usr/bin/env python3

import PyPDF2
pdf1File = open('AssemblyX64.pdf', 'rb')
pdf2File = open('livro-lab-ipv6-nicbr.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pagenum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pagenum)
    pdfWriter.addPage(pageObj)


for pagenum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pagenum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinadoAssembly-IPv6.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
