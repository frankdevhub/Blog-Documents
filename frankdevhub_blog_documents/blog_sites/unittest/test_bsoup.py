#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：test_bsoup.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/9/4 21:34
"""

import logging as log
import unittest

log.basicConfig(level=log.DEBUG)

test_headers = {
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}


class TestBeautifulSoup(unittest.TestCase):

    @staticmethod
    def test_local():
        """测试本地运行环境"""
        log.debug('invoke method -> test_local()')
        html = """
          <html><head><title>The Dormouse's story</title></head>
          <body>
          <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
          <p class="story">Once upon a time there were three little sisters; and their names were
          <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
          <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
          <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
          and they lived at the bottom of a well.</p>
          <p class="story">...</p>
          """
        soup = BeautifulSoup(html)
        assert soup is not None, 'soup cannot be empty'
        # soup = BeautifulSoup(open('index.html'))  # 使用本地文件创建对象
        # log.debug(soup.prettify())


if __name__ == '__main__':
    unittest.main()
