#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：blog_list.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2022/4/4 22:09
"""

import logging as log

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 浏览器请求头
test_headers = {
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

# 测试链接地址
site_domain = 'https://blog.51cto.com/'  # 测试链接域名
blog_home = 'https://blog.51cto.com/oldboy'
# chromedriver浏览器驱动路径
driver_path = 'D://frankdevhub-workspace/chrome-driver/chromedriver.exe'
# 文档存储根目录
download_path = 'D://51cto_blogs/'
# 滚动到浏览器顶部
js_top = 'var q=document.documentElement.scrollTop=0'
# 滚动到浏览器底部
js_bottom1 = 'var q=document.documentElement.scrollTop=10000'
js_bottom2 = 'window.scrollTo(0,document.body.scrollHeight)'
js_bottom3 = 'window.scrollTo(0,4890)'

# 关键字
blog_home_title = '51cto'

log.basicConfig(level=log.INFO)


class Blog_51CTO:

    def __init__(self):
        self._driver = driver_path
        self._url = blog_home
        self._web_driver = None
        self._wait = None

    def scratch_pages(self):
        log.debug('invoke method -> scratch_pages()')
        base_url = self._url
        print(f'url = {base_url}')

        self._web_driver = webdriver.Chrome(self._driver)
        self._web_driver.implicitly_wait(10)
        self._web_driver.maximize_window()
        self._wait = WebDriverWait(self._web_driver, 10)
        self.scratch_docs(self, blog_home_title)

    def scratch_docs(self, link):
        log.debug('invoke method -> scratch_docs()')
        print(f'link = {link}')

        self._web_driver.get(link)
        self._wait.until(EC.title_contains(blog_home_title))
        # 滚动到页面底部
        time.sleep(1)
        # 滚动到页面最底部等待列表页面dom树加载完成
        self._web_driver.execute_script(js_bottom2)
        timeout.sleep(1)
        # 博客列表页 //div[@class='common-article-list']
        doc_list = driver.find_elements(By.XPATH, "//div[@class='common-article-list']")
        for doc in doc_list:
            pass

    def download_docs(self):
        log.debug('invoke method -> download_docs()')
        pass


if __name__ == '__main__':
    scanner = Blog_51CTO()
    scanner.scratch_pages()
