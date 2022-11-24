#!/usr/bin/env python
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

from os import listdir
from os.path import isfile, join
import os

# Определение пути
import sys
path = sys.path[0] + "/"

def pdf_cat(input_files, output_stream):
    input_streams = []
    try:
        # First open all the files, then produce the output file, and
        # finally close the input files. This is necessary because
        # the data isn't read from the input files until the write
        # operation. Thanks to
        # https://stackoverflow.com/questions/6773631/problem-with-closing-python-pypdf-writing-getting-a-valueerror-i-o-operation/6773733#6773733
        for input_file in input_files:
            input_streams.append(open(input_file, 'rb'))
        writer = PdfFileWriter()
        for reader in map(PdfFileReader, input_streams):
            for n in range(reader.getNumPages()):
                writer.addPage(reader.getPage(n))
        writer.write(output_stream)
    finally:
        for f in input_streams:
            f.close()
        output_stream.close()


if __name__ == '__main__':
    if sys.platform == "win32":
        import os, msvcrt
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
    # pdf_cat(sys.argv[1:], sys.stdout)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))] #Создание списка файлов
    print(onlyfiles)
    pdf_cat(onlyfiles, sys.stdout)
