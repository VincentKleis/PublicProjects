from os import mkdir
from bs4 import BeautifulSoup
from requests import get
from urllib.request import urlopen

class scrape_mangatot:
    # chose a starting page and the chapter number of that starting page
    def __init__(self, first_ch_numb: int, first_ch_url: str):
        """Chose a starting page and the chapter number of that starting page

        Args:
            first_ch_numb (int): the chapter number
            first_ch_url (str): page url
        """
        self.current_chapter = first_ch_numb
        self.url = first_ch_url 

    def uppdate_current_chapter(self):
        """Uppdates the current_chapter variable to the chapter number of the current url
        """
        current_chapter = self.current_chapter

        html_page = get(self.url)

        soup = BeautifulSoup(html_page.content, 'html.parser')

        current_chapter = soup.find('title').text[-3:].split(' ')
        if len(current_chapter) == 2:
            current_chapter.pop(0)
        self.current_chapter = int(current_chapter[0])

    def extract_images(self):
        page = urlopen(self.url)

        soup = BeautifulSoup(page, 'html.parser')

        warning = soup.find(class_ = 'viewer')

        images = warning.find_all('img')

        print(warning)
        

    def find_next_chapter(self):
        """Finds the next chapter based on the current url
        """
        html_page = get(self.url)

        soup = BeautifulSoup(html_page.content, 'html.parser')

        next = soup.find(class_ = 'col-12 col-md-4 nav-next')

        self.url = 'https://mangatoto.com' + next.find('a', href = True)['href']


    def scrape_chapters(self, ch_to_scrape:list):
        """Goes through the list of chapters to scrape and removes the ones that were succsesfully scraped

        Args:
            ch_to_scrape (list): list of chapters to scrape
        """
        while self.current_chapter < 974:
            if self.current_chapter == ch_to_scrape[0]:
                chapter = ch_to_scrape.pop(0)
                try:
                    self.extract_images()
                except:
                    failed_chapters.append(chapter)
                    continue
        else:
            self.find_next_chapter()
            self.uppdate_current_chapter()

class scrape_1piecemanga:

    def __init__(self):
        self.path = 'https://ww8.1piecemanga.com/'

    def find_chapter(self, chapter):
        html_page = get(self.path)

        soup = BeautifulSoup(html_page.content, 'html.parser')

        chapter = soup.find(title = f'Permanent Link to One Piece, Chapter {chapter}', href = True)['href']

        return chapter

    def extract_images(self, path):
        html_page = get(path)

        soup = BeautifulSoup(html_page.content, 'html.parser')

        images = soup.find_all(property = 'og:image')

        images = [x['content'] for x in images]

        return images

    def extract_range(self, range):
        failed_chapter = []
        for i in range:
            try:
                path = self.find_chapter(i)

                images = self.extract_images(path)

                new_dir = f'D:\Downloads\Chapter_{i}'

                mkdir(new_dir)

                x = 1

                for image in images:
                    if x<10:
                        x = 0+x
                    if x<100:
                        x = 0+x

                    image_data = get(image).content
                    
                    with open(new_dir+f'\Page_{x}.png', 'wb') as page:
                        page.write(image_data)

                    x += 1
            except:
                failed_chapter.append(i)

        print(f'failed chapters: {failed_chapter}')