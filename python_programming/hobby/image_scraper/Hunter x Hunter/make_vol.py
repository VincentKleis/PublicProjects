from os import mkdir, rename

# chapter_ranges = {1:"1:9", 2:"9:18", 3:"18:27", 4:"27:36", 5:"36:45", 6:"45:55", 7:"55:64", 8:"64:74", 9:"74:84", 10:"84:94", 
# 11:"94:104", 12:"104:116", 13:"116:128", 14:"128:140", 15:"140:152", 16:"152:164", 17:"164:176", 18:"176:188", 19:"188:200", 
# 20:"200:212", 21:"212:224", 22:"224:236", 23:"236:248", 24:"248:261", 25:"261:271", 26:"271:281", 27:"281:291", 28:"291:301", 
# 29:"301:311", 30:"311:321", 31:"321:331", 32:"331:341", 33:"341:351", 34:"351:361",  
chapter_ranges = {35:"361:371", 36:"371:381", 37:"381:391"}

base_path = "/home/vincent/Programing/Python_learning/HOBBY/image_scraper/Hunter x Hunter/images"

volumes = {}

for key in chapter_ranges:
    val_1, val_2 = chapter_ranges[key].split(":")

    chapter_range = range(int(val_1), int(val_2))

    chapters = [f"{base_path}/chapter{i:03d}.cbz" for i in chapter_range]

    volumes[key] = chapters

for key in volumes:
    volume_path = f"{base_path}/volume{key:03d}"

    mkdir(volume_path)

    for chapter in volumes[key]:
        new_chapter_path = f"{volume_path}/{chapter[-14:]}"
        rename(chapter, new_chapter_path)
