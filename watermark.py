#!/usr/bin/env python3.7

import PyPDF2

minutesFile = open('combinadoAssembly-IPv6.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFPage = pdfReader.getPage(0)
pdfWmarkReader = PyPDF2.PdfFileReader(open('watermark.pdf','rb'))
minutesFPage.mergePage(pdfWmarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

result = open('waterMarkCover.pdf','wb')
pdfWriter.write(result)
minutesFile.close()
result.close()
