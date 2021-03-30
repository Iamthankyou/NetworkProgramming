'''

'''


from urllib.request import urlopen
from urllib.request import Request
from http.cookiejar import CookieJar
from urllib.request import build_opener , HTTPCookieProcessor
import datetime

if __name__ == '__main__':
    # Lay header
    #req = Request("http://www.python.org")
    #r = urlopen(req)
    #print(r.getheader('User-Agent'))


    #Lay cookie
    # Noi chua cookie
    cookie_jar = CookieJar();
    # Su dung builder de lay cookie trong header
    opener = build_opener(HTTPCookieProcessor(cookie_jar))

    #Tao http request
    res = opener.open("http://www.youtube.com")
    #print(res)
    #print(cookie_jar)

    ck = list(cookie_jar)
    #print(ck)
    print(ck[0].name)
    print(ck[0].value)
    print(ck[0].domain)
    print(ck[0].path)
    print(ck[0].expires)
    print(datetime.datetime.fromtimestamp(ck[0].expires))
