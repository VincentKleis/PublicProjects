from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping"

html = urlopen(url)

bs = BeautifulSoup(html, 'html.parser')

# finds the see_also section and navigates to its parrent and then to the 3rd sibling wich is the table of links under the see_also section
see_also_table = bs.find('span', {'id': 'See_also'}).parent.next_sibling.next_sibling.next_sibling

# extracts every link from the table under the see_also section and adds the domain adress for wikipedia so that the links are compleete links
links = ['https://en.wikipedia.org'+link.get('href') for link in see_also_table.find_all('a')]

# gets the html for each link in the 'links' list and makes a beautifulsoup element, 
# i then find the first p element that is the first paragraph and gets the text within a print statement
for link in links:
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
    
    try:
        print(bs.find('p').get_text())
    except:
    	print(bs.findall('p')[2].get_text())
        
