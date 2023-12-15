import requests
from urllib.parse import urlencode
from datetime import datetime
import pytz


lat = '-6.175110'
lon = '106.865036'
api_key = 'your api key'


def unix_to_date(unix_timestamp, timezone='Asia/Jakarta'):
    dt_object_utc = datetime.utcfromtimestamp(unix_timestamp)

    utc_timezone = pytz.timezone('UTC')
    dt_object_utc = utc_timezone.localize(dt_object_utc)

    jakarta_timezone = pytz.timezone(timezone)
    dt_object_jakarta = dt_object_utc.astimezone(jakarta_timezone)

    day_date_string = dt_object_jakarta.strftime('%a, %b %d %Y')

    return day_date_string


def get_url(lat, lon, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'

    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
    }

    url_params = urlencode(params)

    complete_url = f"{base_url}?{url_params}"

    return complete_url

def get_data(url):
    response = requests.get(url)
    try:
        return response.json()
    except:
        return {}
    
def parsing_data(data):
    data_list = data.get('list', [])
    if not data_list:
        return
    
    data_kv = {}
    result = ''

    for item in data_list:
        unixtime = item.get('dt', None)
        item_main = item.get('main', {})
        temperatur = item_main.get('temp', None)
        
        if unixtime and temperatur:
            date = unix_to_date(unixtime)
            data_kv.setdefault(date, []).append(temperatur)

    for key in data_kv.keys():
        avg_temp = sum(data_kv[key]) / len(data_kv[key]) - 273.15
        result += f'{key} : {avg_temp:.2f}\u2103\n'

    return result

url = get_url(lat, lon, api_key)
data = get_data(url)
five_day_data = parsing_data(data)

print(five_day_data)


