from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    open = urlopen("https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.YBC-fp8xWas")
    html = BeautifulSoup(open,"html.parser")
    # print(html)

    seven_day = html.find(id= 'seven-day-forecast-list').find_all(class_='forecast-tombstone')
    for day in seven_day:
        name_day = day.find(class_='period-name').get_text()
        print("Name day: ", name_day)
        type_day = day.find(class_='short-desc').get_text()
        print("Type day: ", type_day)
        temp_day = day.find(class_='temp').get_text()
        print("Temp day:", temp_day)
        img_day = day.find('img')
        print(img_day.attrs['src'])
