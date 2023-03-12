from os import listdir, mkdir, rename, rmdir, remove

def pick(base_path, chapters):
    new_path = base_path+'\Countertopp' 
    mkdir(new_path)

    for x in chapters:
        old_name = base_path+f'\Read One Piece - Chapter {str(x)} MangaBuddy_files'
        new_name = new_path+'\Chapter '+str(x)
        rename(old_name, new_name)

    return new_path

def clean(path):
    for folder in listdir(path):
        for item in listdir(f'{path}\{folder}'):
            if item[-4:] != '.jpg' and item[-4:] != '.png' and '.' in item:
                remove(f'{path}\{folder}\{item}')
            elif '.' not in item:
                for sub_item in listdir(f'{path}\{folder}\{item}'):
                    remove(f'{path}\{folder}\{item}\{sub_item}')
                rmdir(f'{path}\{folder}\{item}')

def serve(path, base_path):
    for folder in listdir(path):
        for item in listdir(f'{path}\{folder}'):
            new_item = f'Page_{item[-6:].lstrip("_")}'
            if len(new_item) < 11:
                new_item = f'Page_0{item[-6:].lstrip("_")}'
            if len(new_item) < 11:
                new_item = f'Page_0{item[-6:]}'
            rename(f'{path}\{folder}\{item}', f'{path}\{folder}\{new_item}')
    
        rename(f'{path}\{folder}', f'{base_path}\{folder.replace(" ", "_")}')
        rmdir(path)