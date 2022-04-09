#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：blog_list.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2022/4/4 22:09
"""
import logging as log
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 浏览器请求头
test_headers = {
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

# 测试链接地址
site_domain = 'https://blog.51cto.com/'
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
blog_home_title = 'oldboy'
blog_page_title = '51CTO'

log.basicConfig(level=log.INFO)


class Blog51CTO:

    def __init__(self):
        self._driver = driver_path
        self._url = blog_home
        self._web_driver = None
        self._wait = None

    def scratch_pages(self):
        log.debug('invoke method -> scratch_pages()')
        base_url = self._url
        print(f'url = {base_url}')

        s = Service(self._driver)
        self._web_driver = webdriver.Chrome(service=s)
        self._web_driver.implicitly_wait(10)
        self._web_driver.maximize_window()
        self._wait = WebDriverWait(self._web_driver, 10)

        _link = blog_home
        while _link is not None:
            self.scratch_docs(_link)
            # 获取页面分页控件对象
            next_page = "//ul[@class='pagination']/li[@class='next']/a"
            exist = self._wait.until(EC.visibility_of(self._web_driver.find_element(By.XPATH, next_page)))
            print(f'exist = {exist}')

            if exist is True:
                next_btn = self._web_driver.find_element(next_page)
                next_href = next_btn.find_element('href')
                assert next_href is not None, 'variable next_href cannot be none'
                print(f'next_href = {next_href}')
                _link = next_href

            else:
                driver_link = self._web_driver.current_url
                print(f'process end, last page = {driver_link}')
                os.system(init_cmd)
                print('shutdown')

    def scratch_docs(self, link):
        log.debug('invoke method -> scratch_docs()')
        print(f'link = {link}')

        self._web_driver.get(link)
        self._wait.until(EC.title_contains(blog_home_title))
        time.sleep(1)
        # 滚动到页面最底部等待列表页面dom树加载完成
        self._web_driver.execute_script(js_bottom2)
        time.sleep(1)

        list_xpath = "//div[@class='common-article-list']"
        self._wait.until(EC.presence_of_element_located((By.XPATH, list_xpath)))
        doc_list = self._web_driver.find_elements(By.XPATH, list_xpath)

        assert doc_list is not None, 'variable doc_list cannot be none'
        print("doc_list size = %d" % len(doc_list))

        # 页面列表对象内的文档对象的链接集合
        docs = []
        driver_link = self._web_driver.current_url
        print(f'driver_link = {driver_link}')

        entry = driver_link

        for i in range(1, len(doc_list)):
            article = doc_list[i - 1]

            href = article.find_element(By.XPATH, "div[1]/h3[@class='title']/a")
            doc_title = href.text
            print(f'doc_title = {doc_title}')
            doc_link = href.get_attribute('href')
            print(f'doc_link = {doc_link}')

            assert doc_title is not None, 'variable doc_title cannot be none'
            assert doc_link is not None, 'variable doc_link cannot be none'
            doc = {'title': doc_title, 'link': doc_link}

        docs.append(doc)

        for j in range(1, len(docs)):
            doc = docs[j - 1]
            try:
                self.download_doc(doc['title'], doc['link'])
            except Exception as e:
                print(e)
            finally:
                # 退回到上一级入口,遍历下一个文档对象
                self._web_driver.get(entry)

        print(link_dict)

    def download_doc(self, title, link, entry):
        log.debug('invoke method -> download_docs()')

        assert ctx is not None, 'variable ctx cannot be none'
        assert title is not None, 'variable title cannot be none'
        assert entry is not None, 'variable entry cannot be none'
        print(f'document title = {title}')

        self._web_driver.get(link)
        time.sleep(1)
        self._wait.until(EC.title_contains(blog_page_title))
        # 定位文档文本对象位置
        article_xpath = "//section[@class='detail-content-left']/article[1]"
        article = self._web_driver.find_element(By.XPATH, article_xpath)
        context = article.text
        print(context)

        # 校验文档目录存储读取权限
        access = os.access(download_path, os.F_OK)
        print("path %x access = %d" % (download_path, access))


if __name__ == '__main__':
    init_cmd = "taskkill /im chrome.exe /F"
    print("running command: %s", init_cmd)
    os.system(init_cmd)
    print('process start...')
    try:
        scanner = Blog51CTO()
        scanner.scratch_pages()
    except:
        os.system(init_cmd)
        print('shutdown')
