import requests

if __name__ == '__main__':
    while True:
        city = input('Typing city name: ')
        query = 'q=' + city

        req = requests.get('http://api.openweathermap.org/data/2.5/weather?'
                         + query
                         +'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')

        print(req.json())


