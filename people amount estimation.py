# encoding:utf-8
import os,time

import requests
import base64

'''
人流量统计（动态版）
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_tracking"
img_path = './top-down-test2'

#读图
images = os.listdir(img_path)
images = sorted(images)
data_list = []
# 二进制方式打开图片文件
for i in images:
    f = open(img_path + '/' + i, 'rb')
    img = base64.b64encode(f.read())

    params = {"area": "1,1,543,1,543,400,1,400", "case_id": 1, "case_init": "false", "dynamic": "true", "image": img,"show":"true"}
    access_token = '24.dfad0c9430b24a993bc65909677cb1e8.2592000.1606704739.282335-22904335'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    if response:
        print (response.json())

print('OK!')