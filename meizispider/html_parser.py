#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author  : mundane
# @time    : 2017/5/9 13:16
# @file    : html_parser.py
# @Software: PyCharm Community Edition

import re

from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_soup(self, html_content):
        if html_content is None:
            return None
        return BeautifulSoup(html_content, 'lxml')

    # 获取每个相册的链接地址
    def get_album_urls(self, html_content):
        if html_content is None:
            print('html_content is None')
        soup = self._get_soup(html_content)
        album_urls = []
        li_list = soup.find_all('li')
        for li in li_list:
            try:
                # todo 这里貌似有问题
                a = li.find('a', href=re.compile(r'http://www'))
                if a is not None:
                    # print(a.find('img').attrs['alt'])  #  这个方法和下面那个是一样的
                    # print(a.find('img')['alt'])
                    print(a)
                    data = {'title': a.find('img')['alt'], 'album_url': a['href']}  # 相册名称和链接地址
                    album_urls.append(data)
            except Exception as e:
                print('exception: html_parser_38', e)
        return album_urls

    # 获取每一页的链接地址
    def get_page_urls(self, html_content):
        soup = self._get_soup(html_content)
        page_urls = []
        page_list = soup.find('div', class_='nav-links').find_all('a', class_=re.compile(r'page-numbers'))
        last_page_url = page_list[-2]['href']
        last_index = int(page_list[-2].get_text())
        words = last_page_url.split(r'/')
        index_word = words[-2]
        for index in range(1, last_index + 1):
            page_urls.append(last_page_url.replace(index_word, str(index)))
        return page_urls

    # 获取相册的中最后一页的索引
    def get_last_pic_index(self, html_content):
        if html_content is None:
            print('html_content is None')
        soup = self._get_soup(html_content)
        pic_urls = []
        list = soup.find('div', class_='pagenavi').find_all('a')
        for item in list:
            pic_urls.append(item.get_text())
        return int(pic_urls[-2])

    def get_pic_url(self, html_content):
        if html_content is None:
            print('html_content is None')
        soup = self._get_soup(html_content)
        return soup.find('div', class_='main-image').find('img')['src']
