import requests

if __name__ == '__main__':
    city = input("Nhap thanh pho: ")
    query = 'q=' + city
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?'
                     + query
                     +'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')

    print(r.json())
    print("nhiet do {}".format(r.json()['main']['temp']))
    print("toc do gio {} m/s".format(r.json()['wind']['speed']))
    print("Mo ta {}".format(r.json()['weather'][0]['description']))
    print("Thoi tiet {}".format(r.json()['weather'][0]['main']))