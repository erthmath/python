#!/usr/bin/env python3.7

import PyPDF2

minutesFile = open('combinadoAssembly-IPv6.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(minutesFile)
page = pdfreader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotate.pdf','wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()




