from PIL import Image
from pytesseract import pytesseract
from os import listdir
from time import time

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

base = 'E:\My Drive\Python_learning\HOBBY\kvittering_fix\images'

bongs = []

number = 0

images = listdir(base)

times = []

for image in images:
    if image == 'desktop.ini':
        continue
    start = time()
    
    #Number of immages minus 1 for the desktop.ini if there is a desktop.ini
    if 'desktop.ini' in images:
        length = len(images)-1
    else:
        length = len(images)

    #Open image with PIL
    img = Image.open(f'{base}\{image}')

    #Extract text from image
    text = pytesseract.image_to_string(img, lang='nor')

    bongs.append([number, text])

    number += 1

    times.append(time()-start)

    average_time = sum(times)/(number)

    progres = (number)/length

    time_left = average_time * (length-number)

    print(f'Progress: {round(progres*100)}%\
        \nAverage time: {round(average_time, 2)}s\
        \nProjected time: {round(time_left, 2)}s\n')

for i in bongs:
    print(i[0],'\n', i[1])