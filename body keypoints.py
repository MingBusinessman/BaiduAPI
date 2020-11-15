# encoding:utf-8

import requests
import base64

'''
人体关键点识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
# 二进制方式打开图片文件
f = open('./2person.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img,"show":"ture"}
access_token = '24.dfad0c9430b24a993bc65909677cb1e8.2592000.1606704739.282335-22904335'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())