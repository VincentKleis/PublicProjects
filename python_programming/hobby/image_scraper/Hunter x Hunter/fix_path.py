from os import listdir


base_path = "/home/vincent/Programing/Python_learning/HOBBY/image_scraper/Hunter x Hunter/images"

for volume in listdir(base_path):
    volume_path = f"{base_path}/{volume}"

    