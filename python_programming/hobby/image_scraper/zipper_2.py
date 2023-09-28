from shutil import make_archive
from os import listdir
path = 'G:\My Drive\Python_learning\HOBBY\image_scraper\One_piece\Volumes'

volumes = listdir(path)

for volume in volumes:
    make_archive(f'{path}\{volume}.cbz', 'zip', f'{path}\{volume}')