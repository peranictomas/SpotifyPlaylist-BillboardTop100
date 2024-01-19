# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
  #  print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests
from bs4 import BeautifulSoup
import re

url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print(f"Failed to retrieve the page. Satus code: {response.status_code}")


song_name_div = soup.select(".c-title")
artist_name_div = soup.select(".c-label")

#content_in_divs = soup.select('#title-of-a-story')



#print(content_divs)

songList = []
artistList = []

#artist_names = [item for item in original_list if isinstance(item, str) and not item.isdigit()]

#for div in artist_name_div:
   # stripped_text = div.text.strip()
   # if (
   #     isinstance(stripped_text, str) and
   #     not stripped_text.isdigit() and
   #     stripped_text.upper() not in ['-','RE-','ENTRY','NEW', 'RE-ENTRY']
   # ):
        #print("Filtered:", stripped_text)
    #else:
        #print("Not filtered:", stripped_text)

for div in artist_name_div:
    # had to clean the string as there was a lot of white space and a new line for RE- ENTRY text
    cleaned_string = re.sub(r'\s', '', div.text.strip())
    if cleaned_string not in ['RE-ENTRY', 'NEW', '-'] and not cleaned_string.isdigit():
        artistList.append(cleaned_string)

for div in song_name_div:
    if div.text.strip() not in ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:', 'Gains in Weekly Performance',
                        'Additional Awards']:
        songList.append(div.text.strip())


top_100_artists = artistList[0:100]
top_100_songs = songList[1:101]

top_100_charts = dict(zip(top_100_songs, top_100_artists))

print(top_100_charts)
