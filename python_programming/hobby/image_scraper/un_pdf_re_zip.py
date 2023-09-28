import os
import fitz  # pip install --upgrade pip; pip install --upgrade pymupdf
from tqdm import tqdm # pip install tqdm
import shutil

workdir = "G:\My Drive\Python_learning\HOBBY\image_scraper\One_piece\Compressed"

for each_path in os.listdir(workdir):
    os.mkdir(workdir+'\\'+each_path[:-4])
    if ".pdf" in each_path:
        doc = fitz.Document((os.path.join(workdir, each_path)))

        for i in tqdm(range(len(doc)), desc="pages"):
            for img in tqdm(doc.get_page_images(i), desc="page_images"):
                xref = img[0]
                image = doc.extract_image(xref)
                pix = fitz.Pixmap(doc, xref)
                pix.save(os.path.join(workdir+'\\'+each_path[:-4], "%s_p%s.png" % (each_path[:-4], i)))

        shutil.make_archive(workdir+'\\'+each_path[:-4]+'.cbz', 'zip', workdir+'\\'+each_path[:-4])
        os.rename(workdir+'\\'+each_path[:-4]+'.cbz.zip', workdir+'\\'+each_path[:-4]+'.cbz')
        shutil.rmtree(workdir+'\\'+each_path[:-4])