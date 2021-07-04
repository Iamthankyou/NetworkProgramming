import requests
from urllib.request import build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar

if __name__ == '__main__':
    cookie = CookieJar()
    openner = build_opener(HTTPCookieProcessor(cookie))

    res = openner.open('http://www.youtube.com')

    ck = list(cookie)
    print(cookie)
    print(ck[0].name)