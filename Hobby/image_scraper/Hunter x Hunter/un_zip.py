from os import listdir, mkdir, remove
from zipfile import ZipFile


base_path = "/home/vincent/Programing/Python_learning/HOBBY/image_scraper/Hunter x Hunter/images"

for volume in listdir(base_path):
    if volume == "volume012":
        continue
    volume_path = f"{base_path}/{volume}"

    for chapter in listdir(volume_path):
        chapter_path = f"{volume_path}/{chapter[:-4]}"

        with ZipFile(f"{chapter_path}.cbz", "r") as zip:
            mkdir(chapter_path)

            zip.extractall(chapter_path)

            remove(f"{chapter_path}.cbz")