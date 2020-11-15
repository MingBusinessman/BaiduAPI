# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import requests
import base64
import json
from pprint import pprint
import time
import io
from io import BytesIO
import cv2
import numpy as np
from PIL import Image
import glob

# client_id 为官网获取的AK， client_secret 为官网获取的SK
api_key = '02YtCG7XbgFUiQSby7Q5qLG3'
secret_key = 'AO2nvbYyIE3vsab3K1OoCWRdiSIUgkoQ'


class Traffic_flowRecognizer(object):
    def __init__(self, api_key, secret_key):
        self.access_token = self._get_access_token(api_key=api_key, secret_key=secret_key)
        self.API_URL = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_tracking' + '?access_token=' + self.access_token
        # 获取token

    @staticmethod
    def _get_access_token(api_key, secret_key):
        api = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(api_key, secret_key)
        rp = requests.post(api)
        if rp.ok:
            rp_json = rp.json()
            print(rp_json['access_token'])
            return rp_json['access_token']
        else:
            print('=>Error in getaccesstoken!')

    def get_result(self, params):
        rp = requests.post(self.API_URL, data=params)
        if rp.ok:
            print('= >Success! gotresult: ')
            rp_json = rp.json()
            pprint(rp_json)
            return rp_json
        else:
            print('=>Error! tokeninvalid or networkerror!')
            print(rp.content)
            return None
            # 人流量统计

    def detect(self):
        ###对视频进行抽帧后，抽帧频率5fps，连续读取图片
        WSI_MASK_PATH = 'top-down-test2'  # 存放图片的文件夹路径
        images = os.listdir(WSI_MASK_PATH)
        images = sorted(images)
        data_list = []
        for i in images:
            f = open(WSI_MASK_PATH + '/' + i, 'rb')
            img_str = base64.b64encode(f.read())
            data_list.append(img_str)
            params = {'dynamic': 'true', 'area': '1,1,543,1,543,400,1,400', 'case_id': 1213, 'case_init': 'false',
                      'image': data_list, 'show': 'true'}
            tic = time.clock()
            rp_json = self.get_result(params)
            toc = time.clock()
            print('单次处理时长: ' + '%.2f' % (toc - tic) + ' s')
            img_b64encode = rp_json['image']
            img_b64decode = base64.b64decode(img_b64encode)  # base64解码
            # 显示检测结果图片
            #            image = io.BytesIO(img_b64decode)
            #            img = Image.open(image)
            #            img.show()
            # 存储检测结果图片
            file = open('./test_result/' + str(i) + '.jpg', 'wb')
            file.write(img_b64decode)
            file.close()


if __name__ == '__main__':
    recognizer = Traffic_flowRecognizer(api_key, secret_key)
    recognizer.detect()