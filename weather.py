import json
import requests
import sys

bot_name  = ''
webhook = ''
url = ''

def check_variables():
    if bot_name == '':
        print('bot_nameにボットの名前が登録されていません')
        sys.exit()
    elif webhook == '':
        print('webhookにSlackのIncomming WebhookんpURLが登録されていません')
        sys.exit()
    elif url == '':
        print('urlにlivedoor天気のJSONのURLが登録されていません')
        sys.exit()

def get_json(url):
    res = requests.get(url)
    json = res.json()
    return json

def make_message(json):
    date = json['forecasts'][1]['date']
    weather = json['forecasts'][1]['telop']
    max_temperature = json['forecasts'][1]['temperature']['max']['celsius']
    min_temperature = json['forecasts'][1]['temperature']['min']['celsius']
    return '@channel ' + date + ' ' + weather + ' '  + max_temperature + '℃ ' + min_temperature + '℃'

def post_to_slack(message):
    data = json.dumps({
        'text': message,
        'username': bot_name,
    })
    requests.post(webhook, data)

def main():
    check_variables()
    json = get_json(url)
    post_to_slack(make_message(json))

if __name__ == '__main__':
    main()
