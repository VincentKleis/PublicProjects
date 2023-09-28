from os import listdir, rename

path = 'G:\My Drive\Python_learning\HOBBY\image_scraper\One_piece\Volumes'

Volumes = listdir(f'{path}')

for volume in Volumes:
    if volume[-4:] == '.zip':    
        rename(f'{path}\{volume}', f'{path}\{volume[:-4]}')