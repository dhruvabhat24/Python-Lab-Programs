from PyPDF2 import PdfReader, PdfWriter
num = int(input("Enter the number of pages you need to combine from multiple PDFs: "))
Pdf1=open('UNIX SYL.pdf','rb')
Pdf2=open('PYTHON SYL.pdf','rb')
pdf_writer = PdfWriter()
pdf1_reader = PdfReader(Pdf1)
page = pdf1_reader.getPage[num-1]
pdf_writer.addPage(page)
pdf2_reader = PdfReader(Pdf2)
page = pdf2_reader.getPage[num-1]
pdf_writer.addPage(page)
with open('output.pdf', 'wb') as output:
    pdf_writer.write(output)