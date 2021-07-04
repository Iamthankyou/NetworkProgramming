import requests

if __name__ == '__main__':
    r = requests.get('http://python.org')
    print(r.headers)
