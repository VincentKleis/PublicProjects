from genericpath import isdir
from io import BytesIO
from PIL import Image
from os import mkdir
from requests import get

images_path = "/home/vincent/Programing/Python_learning/HOBBY/image_scraper/Hunter x Hunter/images"

init_url = "https://cdn.watchgoblinslayer.com/file/mangap/1828/1"

# "c" is chapter number and "p" is page number
for c in range(1, 1000):
    for p in range(1, 100):
        # the ":04d" part of the f string is to format the number with leading zeros
        mod = f"{c:04d}000/{p}.jpg"

        response = get(f"{init_url}{mod}")

        if str(response) == "<Response [404]>":
            break
        
        img = Image.open(BytesIO(response.content))

        if isdir(f"{images_path}/chapter{c:03d}/") == False:
            mkdir(f"{images_path}/chapter{c:03d}/")

        img.save(f"{images_path}/chapter{c:03d}/page{p:03d}.jpg")