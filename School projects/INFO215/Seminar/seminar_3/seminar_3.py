import urllib.request
from bs4 import BeautifulSoup

# Open the URL
url = "https://simple.wikipedia.org/wiki/Abbey_Road"
response = urllib.request.urlopen(url)

# Read the HTML content of the page
html = response.read()

# Parse the HTML content of the page
soup = BeautifulSoup(html, "html.parser")

# We can use the .find() function to find a single match for a tag. (It finds the
# first match in the html).
#.text gets the text between the html tags.

headline = soup.find("h1").text
#print(headline)

# Similarily we can use .find_all to find all matches of the tag.

test = soup.find_all("p")
#for a in test:
#    print(a)


# track length in minuts calculated with the individual track lengths

# tracklists = soup.find_all("table", {"class": "tracklist"})

# album_length = 0
# for side in tracklists:
#     for x in side:
#         if len(x) == 1:
#             continue
#         for track_elements in x:
#             if len(track_elements) != 8:
#                 continue
#             for element in track_elements:
#                 if track_elements.index(element) == 6:
#                     if element.text == "Length":
#                         continue
#                     time = element.text.split(":")
#                     album_length += int(time[0])
#                     # seconds of the 
#                     album_length += int(time[1]) / 60

# finding album duration throuhg (task 1)
table = soup.find("table", {"class": "infobox vevent haudio"})
duration = table.find("span", {"class": "duration"})
print(duration.text)

# finding genre text (task 2)
genres = table.find("td", {"class": "infobox-data category hlist"})
genre_list = genres.find_all("a")
genre_text = []
for genre in genre_list:
    genre_text.append(genre.text)

print(genre_text)

# find genre title (task 3)
genre_title = []
for genre in genre_list:
    genre_title.append(genre["title"])

print(genre_title)

# side one titles (task 4)
side_1 = soup.find("table", {"class":"tracklist"})
print(side_1[1])

