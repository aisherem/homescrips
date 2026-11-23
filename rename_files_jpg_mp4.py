# создание пути
import pathlib
from pprint import pprint
from PIL import Image
from os import listdir
from os.path import isfile, join
import os
from datetime import datetime, timedelta

source_name = "" # Имя фотоаппрата/телефона

# os.rename('a.txt', 'b.kml')

def transformdate(data):
    # 2021:12:29 14:07:22
    return  (data.replace(":", "-"))

def sdvig_vremeni(date_string, operation, shift_t):
    date_format = "%Y:%m:%d %H:%M:%S"
    try:
        dt_object = datetime.strptime(date_string, date_format)
    except ValueError as e:
        print(f"Ошибка при парсинге даты: {e}")
        print("Убедитесь, что формат строки '%Y:%m:%d %H:%M:%S' соответствует вашей дате.")
        return None
    time_delta = timedelta(seconds=shift_t)
    if operation == "+":
        new_dt_object = dt_object + time_delta
    else:
        new_dt_object = dt_object - time_delta
    new_date_string = new_dt_object.strftime(date_format)

    return new_date_string

path = "/mnt/c/PHOTO/"
path = "/mnt/c/2025/"
path = "/mnt/c/2026-07-29/"

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))] #Создание списка файлов

list_jpg = [] # создание jpg списка файлов
list_mp4 = [] # создание mp4 списка файлов
list_mp4_2 = [] # создание mp4 списка файлов
list_mov = [] # создание mp4 списка файлов

for f in onlyfiles:
    if f.endswith(".jpg") or f.endswith(".JPG") or  f.endswith(".jpeg"):
        list_jpg.append(f)
    elif f.startswith('VID_') and f.endswith('.mp4'):
        list_mp4.append(f)
    elif f.endswith('.mp4'):
        list_mp4_2.append(f)
    elif f.endswith('.mov'):
        list_mov.append(f)


for f in list_jpg:
    im = Image.open(f"{path}{f}")
    source_name = ""
    # Протестировать ня скриншотах, так как они подписывались последним source_nameы
    try:
        camera =  im._getexif()[272]
        if 'SM-A515F' in camera: source_name = 'a51'
        if 'SM-A505FM' in camera: source_name = 'a50'
        if 'iPhone 7' in camera: source_name = 'iph7'
        if 'iPhone 8' in camera: source_name = 'iph8'
        if 'iPhone 11 Pro' in camera: source_name = 'iph11'
        if 'iPhone 13' in camera: source_name = 'iph13'
        if 'iPhone 15' in camera: source_name = 'iph15'
        if 'SM-A325F' in camera: source_name = 'a32'
        if 'CH7n' in camera: source_name = 'c18p'
        if 'CK7n' in camera: source_name = 'c20p'
    except: pass
    # print(camera, source_name)
    try: 
        if im._getexif()[36867]:
            data = im._getexif()[36867]
            # data_shift = 86569
            # data = sdvig_vremeni(data, "+", 86569)
            data_new = transformdate(data)
            if source_name: temp_file_name = f'{data_new}' + "_" + source_name
            else: temp_file_name = f'{data_new}'
            count = 1
            data_new = str(temp_file_name)
            while os.path.exists(f'{path}{data_new}.jpg'):
                data_new = temp_file_name + "-" +str(count)
                count += 1
            os.rename (f"{path}{f}", f'{path}{data_new}.jpg')
            print (f"{f} - > {data_new}.jpg")
        else:
            print (f'{f} has not exif')
    except:
        print (f'{f} has not exif')
for f in list_mp4:
    # VID_20211229_140550.mp4 
    f1 = f.split(".")[0]
    filename = f1.split("_")
    if len(filename) == 3:
        _, d, t = filename
        add = None
    elif len(filename) == 4:
         _, d, t, add = filename
    date = d[0]+d[1]+d[2]+d[3] + "-" + d[4]+d[5] + "-" + d[6]+d[7] 
    time = t[0]+t[1] + "-" + t[2]+d[3] + "-" + t[4] + t[5]
    if add:
        temp_file_name =  f'{date} {time} {add}'
    else:
        temp_file_name =  f'{date} {time}'
    count = 1
    data_new = str(temp_file_name)
    while os.path.exists(f'{path}{data_new}.mp4'):
        data_new = temp_file_name + "-" +str(count)
        count += 1
    os.rename (f"{path}{f}", f'{path}{data_new}.mp4')
    print (f"{f} - > {data_new}.mp4")

for f in list_mp4_2:
    # VID_20211229_140550.mp4 
    f1 = f.split(".")[0]
    if "None" in f1:
        print(f1)
        date, time, n = f1.split()
        temp_file_name =  f'{date} {time}'
    elif "_" in f1:
        d, t, *num = f1.split("_")
        date = d[0]+d[1]+d[2]+d[3] + "-" + d[4]+d[5] + "-" + d[6]+d[7] 
        time = t[0]+t[1] + "-" + t[2]+d[3] + "-" + t[4] + t[5]
        temp_file_name =  f'{date} {time}'
    count = 1
    data_new = str(temp_file_name)
    while os.path.exists(f'{path}{data_new}.mp4'):
        data_new = temp_file_name + "-" +str(count)
        count += 1
    os.rename (f"{path}{f}", f'{path}{data_new}.mp4')
    print (f"{f} - > {data_new}.mp4")

for f in list_mov:
    # 2025-01-04 13.16.44.mov
    # f1 = f.split(".m")[0]
    temp_file_name = f.replace(".", "-")
    temp_file_name = temp_file_name.replace("-mov", ".MOV")
    count = 1
    data_new = str(temp_file_name)
    while os.path.exists(f'{path}{data_new}'):
        data_new = temp_file_name + "-" +str(count)
        count += 1
    os.rename (f"{path}{f}", f'{path}{data_new}')
    print (f"{f} - > {data_new}")
