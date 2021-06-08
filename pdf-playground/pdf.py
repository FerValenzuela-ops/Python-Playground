import PyPDF2
import sys
import os
# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     #print(reader.getPage(1))#
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)


archives = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
# pdf_combiner(inputs)


def pdfwatermark(archives):

    pdf = PyPDF2.PdfFileReader(open(f'{archives[0]}', 'rb'))
    pdf_pages = pdf.getNumPages()
    wtr = PyPDF2.PdfFileReader(open(f'{archives[1]}', 'rb'))
    pdf_writer = PyPDF2.PdfFileWriter()
    for page in range(pdf_pages):
        pdf_page = pdf.getPage(page) #obtaining actual page
        pdf_page.mergePage(wtr.getPage(0)) #create new page with watermark merged
        pdf_writer.addPage(pdf_page)

    with open(f'{archives[2]}', "wb") as filehandle_output:
            # write the watermarked file to the new file
        pdf_writer.write(filehandle_output)

pdfwatermark(archives)
