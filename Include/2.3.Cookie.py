import requests
from bs4 import BeautifulSoup

from urllib.request import urlopen

if __name__ == '__main__':
    ''' VI DU
    html = urlopen("https://www.wikipedia.org/wiki/python")
    bs = BeautifulSoup(html,"html.parser")
    print(bs.prettify())

    for link in bs.find_all("a"):
        if 'href' in link.attrs:
            print(link.attrs['href']);
    '''
    html = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.YBC-fp8xWas')
    bs = BeautifulSoup(html.content, "html.parser")
    dubao = bs.find(id = 'seven-day-forecast')
    dubao1 = dubao.find_all(class_ = 'tombstone-container')

    tonight = dubao1[0]
    #print(tonight.prettify())
    img  = tonight.find('img')
    mota = img['title']
    A = [1, 2, 3,4,5,6,7]
    for i in A:
        tonight = dubao1[i]

        period = tonight.find(class_ = 'period-name').get_text()
        short_desc = tonight.find(class_ = 'short-desc').get_text()
        temp = tonight.find(class_ = 'temp').get_text()

        print(period)
        print(short_desc)
        print(temp)

