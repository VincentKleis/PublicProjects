from os import listdir, rmdir, remove
from zipfile import ZipFile

base_path = "image_scraper/Hunter x Hunter/images"

for chapter in listdir(base_path):
    if chapter[-3:] == "cbz":
        continue

    chapter_path = f"{base_path}/{chapter}"

    pages = []

    for page in listdir(chapter_path):
        pages.append(page)
    
    pages.sort()
    
    with ZipFile(f"{chapter_path}.cbz", "w") as zip:
        for page in pages:
            zip.write(f"{chapter_path}/{page}")

    for page in listdir(chapter_path):
        remove(f"{chapter_path}/{page}")

    rmdir(chapter_path)
    break