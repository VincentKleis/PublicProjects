from bs4 import BeautifulSoup
from requests import get
from urllib.request import urlopen

ch_to_scrape = [x for x in range(317, 378)] + [x for x in range(381, 389)] + [315] + [x for x in range(270,276)] + [267]
ch_to_scrape += [x for x in range(257, 265)] + [x for x in range(248, 256)] + [x for x in range(238, 247)] 
ch_to_scrape += [x for x in range(222, 237)] + [217, 203, 202, 200] + [x for x in range(288, 296)] 
ch_to_scrape += [x for x in range(138, 146)] + [121, 122, 123, 124, 125, 126] + [113, 114, 115, 116, 117] +[106, 107]
ch_to_scrape.sort()
failed_chapters = []

# class to scrape the site mangatot
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

        # images = warning.find_all('img')

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



test = scrape_mangatot(1, 'https://mangatoto.com/chapter/683929')
test.extract_images()