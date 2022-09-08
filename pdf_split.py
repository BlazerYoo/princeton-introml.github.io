## TO DO: change this number if the number of chapters/parts is different
NUM_CHAPTERS = 20
PART_MARKERS = ['I', 'II', 'III', 'IV', 'V', 'VI']

from PyPDF2 import PdfFileReader, PdfFileWriter
pdf = PdfFileReader("files/COS324_Course_Notes.pdf")

## Find the page number where the Table of Contents starts
toc_page_no = 0
while toc_page_no < pdf.getNumPages():
    lines = pdf.pages[toc_page_no].extract_text().split('\n')
    if lines[0] == 'Contents':
        break
    toc_page_no += 1

## Find the start page of each chapter and each part
lines = pdf.pages[toc_page_no].extract_text().split('\n')
line_no = 0
chap_no = 1
page_split_markers = []

while chap_no <= NUM_CHAPTERS:
    line = lines[line_no]
    page_no = line.split(' ')[-1]
    for part_no in PART_MARKERS:
        if line.startswith(part_no + ' '):
            if not part_no == 'I':
                page_split_markers[-1].append(int(page_no))
            page_split_markers.append([int(page_no)])

    if line.startswith(str(chap_no) + ' '):
        page_split_markers[-1].append(int(page_no))
        chap_no += 1

    line_no += 1

    if line_no == len(lines):
        toc_page_no += 1
        lines = pdf.pages[toc_page_no].extract_text().split('\n')
        line_no = 0

page_split_markers[-1].append(pdf.getNumPages() + 1)

## Save files for individual chapters and parts
part_no = 1
chap_no = 1
for part in page_split_markers:
    pdf_writer = PdfFileWriter()
    for page in range(part[0], part[-1]):
        pdf_writer.addPage(pdf.getPage(page - 1))
    
    outputFilename = "files/part{}.pdf".format(part_no)
    with open(outputFilename, "wb") as out:
        pdf_writer.write(out)

    part_no += 1
    print("created", outputFilename)

    for i in range(1, len(part) - 1):
        pdf_writer = PdfFileWriter()
        for page in range(part[i], part[i + 1]):
            pdf_writer.addPage(pdf.getPage(page - 1))

        outputFilename = "files/ch{}.pdf".format(chap_no)
        with open(outputFilename, "wb") as out:
            pdf_writer.write(out)

        chap_no += 1
        print("created", outputFilename)
