#search_pypi.py - Opens several search results.
from distutils.errors import LinkError
import requests
import sys
import webbrowser
import bs4

print('Searching...') # display text while downloading the search results page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])) # 'https://google.com/search?q=' 
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
link_elems = soup.select('.package-snippet')

num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)
