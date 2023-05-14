import requests 

while True:
    city = input('City: ')
    url = 'https://wttr.in/{}'.format(city)
    res = requests.get(url)
    print(res.text)