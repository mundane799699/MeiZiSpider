#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author  : mundane
# @time    : 2017/5/9 10:23
# @file    : GetMeiZi.py
# @Software: PyCharm Community Edition

from meizispider import html_downloader
from meizispider import html_parser
import os
import requests


class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()

    def craw(self, url):
        html_content = self.downloader.download_html(url)
        page_urls = self.parser.get_page_urls(html_content)
        for page_url in page_urls:
            # page_url
            # http://www.mzitu.com/xinggan/page/1/
            page_html_content = self.downloader.download_html(page_url)
            if page_html_content is None:
                print('page_html_content is None')
                continue
            album_url_and_title = self.parser.get_album_urls(page_html_content)
            for album_url_and_title in album_url_and_title:
                # album_url
                # http://www.mzitu.com/91956
                album_url = album_url_and_title['album_url']
                album_title = album_url_and_title['title']
                album_html_content = self.downloader.download_html(album_url)
                if album_html_content is None:
                    print('album_html_content is None')
                    continue
                last_pic_index = self.parser.get_last_pic_index(album_html_content)
                print("创建相册：" + album_title)
                try:
                    os.mkdir(album_title)
                except Exception as e:
                    print('exception:', e)
                    continue
                for index in range(1, last_pic_index + 1):
                    # pic_page_url
                    # http://www.mzitu.com/91956/65
                    pic_page_url = '%s/%d' % (album_url, index)
                    pic_page_html_content = self.downloader.download_html(pic_page_url)
                    if pic_page_html_content is None:
                        print('pic_page_html_content is None')
                        continue
                    pic_url = self.parser.get_pic_url(pic_page_html_content)
                    filename = pic_url.split('/')[-1]
                    img = self.downloader.download_pic(pic_url)
                    name = str(album_title + '/' + filename)
                    if img is None:
                        continue
                    print('开始下载', pic_url)
                    with open(name, 'wb') as f:
                        f.write(img.content)


if __name__ == '__main__':
    root_url = 'http://www.mzitu.com/xinggan'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
