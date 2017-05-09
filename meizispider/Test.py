#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author  : mundane
# @time    : 2017/5/9 21:19
# @file    : Test.py
# @Software: PyCharm Community Edition

import os
import requests
from meizispider import html_downloader

if __name__ == '__main__':
    dir = 'test'
    try:
        os.mkdir(dir)
    except Exception as e:
        print('exception:', e)
    pic_url = 'http://i.meizitu.net/2017/05/08a64.jpg'
    filename = pic_url.split('/')[-1]
    img = requests.get(pic_url)
    name = str(dir+'/'+filename)
    with open(name, 'wb') as f:
        f.write(img.content)

