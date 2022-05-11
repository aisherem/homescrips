# создание пути
import pathlib
from pprint import pprint
from PIL import Image
from os import listdir
from os.path import isfile, join
import os

source_name = "" # Имя фотоаппрата/телефона

# os.rename('a.txt', 'b.kml')

def transformdate(data):
    # 2021:12:29 14:07:22
    return  (data.replace(":", "-"))

def get_path():
    path = pathlib.Path(__file__).parent.absolute()
    path = f'{path}/'
    return path
path = get_path()
# print (path)
# path = "/mnt/c/фото/Новый год. Школьники/"
path = "/mnt/c/tempo/"

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))] #Создание списка файлов

list_jpg = [] # создание jpg списка файлов
list_mp4 = [] # создание mp4 списка файлов
list_mp4_2 = [] # создание mp4 списка файлов

for f in onlyfiles:
    if f.endswith(".jpg") or f.endswith(".JPG"):
        list_jpg.append(f)
    elif f.startswith('VID_') and f.endswith('.mp4'):
        list_mp4.append(f)
    elif f.endswith('.mp4'):
        list_mp4_2.append(f)


for f in list_jpg:
    im = Image.open(f"{path}{f}")
    try:
        camera =  im._getexif()[272]
        if 'SM-A515F' in camera: source_name = 'a51'
        if 'SM-A505FM' in camera: source_name = 'a50'
        if 'iPhone 7' in camera: source_name = 'iph7'
        if 'SM-A325F' in camera: source_name = 'a32'
    except: pass
    # print(camera, source_name)
    try: 
        if im._getexif()[36867]:
            data = im._getexif()[36867]
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
    _, d, t = f1.split("_")
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

for f in list_mp4_2:
    # VID_20211229_140550.mp4 
    f1 = f.split(".")[0]
    # print(f1)
    if "_" in f1:
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
