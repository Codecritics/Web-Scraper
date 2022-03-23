from collections import defaultdict

from bs4 import BeautifulSoup
from requests import get

if __name__ == '__main__':
    print("Input the URL:")
    url = input()

    movie = defaultdict(str)

    r = get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    if str(r.status_code).startswith('4') or 'title' not in url:
        print("Invalid movie page!")
    else:
        soup = BeautifulSoup(r.content, 'html.parser')
        movie['title'] = soup.find('h1').text
        movie['description'] = soup.find('span', {'data-testid': 'plot-l'}).text

        print(dict(movie))
