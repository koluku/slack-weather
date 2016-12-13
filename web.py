import requests
import json

def get_json(url):
    res = requests.get(url)
    json = res.json()
    return json

def post_to_slack(message):
    data = json.dumps({
        'text': message,
        'username': 'weather_bot',
    })
    requests.post(WEBHOOK, data)

def main():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=017010'
    json = get_json(url)
    date = json['forecasts'][1]['date']
    weather = json['forecasts'][1]['telop']
    max_temperature = json['forecasts'][1]['temperature']['max']['celsius']
    min_temperature = json['forecasts'][1]['temperature']['min']['celsius']
    post_to_slack('@channel ' + date + ' ' + weather + ' '  + max_temperature + '℃ ' + min_temperature + '℃')

if __name__ == '__main__':
    main()
