from PyPDF2 import PdfFileMerger
import os

from os import listdir
from os.path import isfile, join

merger = PdfFileMerger()


import sys
path = sys.path[0] + "/"

name = "theModalBook"

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))] #Создание списка файлов

new_onlyfiles = list()
for file_name in onlyfiles:
    if "pdf" in file_name:
        n = file_name.replace(name, "")
        n = n.split('.')[0]
        if len(n)<2: n = "0"+n
        os.rename (f"{path}{file_name}", f"{path}{name}{n}.pdf")

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))] #Создание списка файлов
onlyfiles.sort()


for file_name in onlyfiles:
    if "pdf" in file_name:
        file_name = path + file_name
        # print (file_name)
        merger.append(file_name)
merger.write(f"{path}merged_all_pages.pdf")
merger.close()