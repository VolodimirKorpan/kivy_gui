import requests

r = requests.get('http://127.0.0.1:8000/AT25%?pob=27.07.2020 09:00').json()
for i in r:
    print(i['date_time'] + '  ' + i['plate'])