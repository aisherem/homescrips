import pathlib
from os import listdir
from os.path import isfile, join
from shutil import copyfile, move
import os
def get_path():
    path = pathlib.Path(__file__).parent.absolute()
    path = f'{path}/'
    return path
path = get_path()
# print (path)
# path = "/mnt/c/фото/Новый год. Школьники/"
path = "/mnt/c/tmp/f/"


def make_dir(file):
    dir = file.split()[0]
    dir = dir.replace('-', '_')
    return (dir)
    
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))] #Создание списка файлов

list_jpg = [] # создание jpg списка файлов
list_mp4 = [] # создание mp4 списка файлов

for f in onlyfiles:
    if f.endswith(".jpg") or f.endswith(".JPG"):
        list_jpg.append(f)
    elif f.endswith('.mp4') or f.endswith('.MOV') or f.endswith('.MP4'):
        list_mp4.append(f)

for f in list_jpg:
    dir = make_dir(f)
    if not os.path.exists(f'{path}{dir}'):
        os.makedirs(f'{path}{dir}')
    move(f'{path}{f}', f'{path}{dir}/{f}')
    print (f'Move {f}')

for f in list_mp4:
    dir = make_dir(f)
    if not os.path.exists(f'{path}{dir}'):
        os.makedirs(f'{path}{dir}')
    move(f'{path}{f}', f'{path}{dir}/{f}')
    print (f'Move {f}')

