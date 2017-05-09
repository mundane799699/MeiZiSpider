#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author  : mundane
# @time    : 2017/5/8 14:05
# @file    : html_downloader.py
# @Software: PyCharm Community Edition

import requests



class HtmlDownloader(object):

    def download_html(self, url):
        if url is None:
            return None

        #  浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None
        return response.text

    def download_pic(self, url):
        if url is None:
            return None
        try:
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
            return requests.get(url, headers=headers)
        except Exception as e:
            print('exception:', e)
            return None
