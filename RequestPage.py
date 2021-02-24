import requests

if __name__ == '__main__':
    query = {'q':'river','min_width':'800','min_height':'800'}

    req = requests.get('http://pixabay.com/images/search',params=query)

    print(req.url)