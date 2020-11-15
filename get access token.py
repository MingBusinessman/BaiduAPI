# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=02YtCG7XbgFUiQSby7Q5qLG3&client_secret=AO2nvbYyIE3vsab3K1OoCWRdiSIUgkoQ'
response = requests.get(host)
if response:
    print(response.json())