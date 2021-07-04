from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    open = urlopen("http://vi.wikipedia.org/wiki/Trang_Ch%C3%ADnh")
    html = BeautifulSoup(open,"html.parser")
    # print(html)

    for link in html.find_all("a"):
        if 'href' in link.attrs:
            print(link)