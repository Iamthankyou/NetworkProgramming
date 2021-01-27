from http.cookiejar import CookieJar
from urllib.request import build_opener,HTTPCookieProcessor

if __name__ == '__main__':
    cookie_jar = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cookie_jar))
    opener.open('http://github.com')
    cookies = list(cookie_jar)

    for i in cookies:
        print(i)