from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

if __name__ == '__main__':
    html = urlopen("https://www.wikipedia.org/wiki/python")
    bs = BeautifulSoup(html)
    print(bs)

