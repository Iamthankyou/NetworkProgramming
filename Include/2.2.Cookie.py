import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    query = {'q': 'river', 'min_width' : '800' , 'min_height' : '600'}

    req = requests.get('https://pixabay.com/vi/photos/search', params = query)
    print(req.url)