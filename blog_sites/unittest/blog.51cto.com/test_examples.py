#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：test_examples.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/10/8 22:14
"""
import logging as log
import unittest

import requests
from lxml import etree

log.basicConfig(level=log.DEBUG)
test_headers = {
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
# test_blogs
test_blog_example = "https://blog.51cto.com/oldboy"  # https://blog.51cto.com/oldboy 博客个人空间页面(测试样例)
# test_docs
test_doc_link = "https://blog.51cto.com/oldboy/1189530"  # https://blog.51cto.com/oldboy/1189530  博客文档内容页面(测试样例)
test_docs_list_xpath = "//div[@class='common-article-list']"  # //div[@class="common-article-list"] 博客个人空间页面下当前页下的文档对象集合
test_pagination_tags_xpath = "//ul[@class='pagination']/li/a"  # //ul[@class='pagination']/li/a 博客个人空间当前页页脚分页控件对象
# test_documents
test_doc_title_xpath = "//div[@class='title']/h1"  # //div[@class='title']/h1 博客文档对象的标题


# 测试获取博客文档以及相关属性
class TestExamples(unittest.TestCase):

    @staticmethod
    def test_get_dom_tree() -> etree:
        log.debug('invoke method -> test_get_dom_tree()')
        response = requests.get(url=test_blog_example, headers=test_headers)
        page_context = response.text
        tree = etree.HTML(page_context)
        assert tree is not None, 'xml tree cannot be none'
        print(type(tree))
        return tree

    @staticmethod
    def test_get_page_doc_list():
        # 测试抓取博客网页对象中的博文简介列表对象
        log.debug('invoke method -> test_get_page_doc_list()')
        docs_xpath = test_docs_list_xpath
        print(f'using xpath = {str(docs_xpath)}')
        response = requests.get(url=test_blog_example, headers=test_headers)
        page_context = response.text
        docs_tree = etree.HTML(page_context)

        assert docs_tree is not None, 'xml tree cannot be none'
        page_docs = docs_tree.xpath(docs_xpath)
        assert page_docs is not None, 'page_docs cannot be none'
        print(f'page_docs size = {len(page_docs)}')
        return

    @staticmethod
    def test_get_pagination_tags():
        # 测试依据Xpath表达式捕获页脚分页标签对象
        log.debug('invoke method -> test_get_pagination_tags()')
        page_tree = TestExamples.test_get_dom_tree()
        assert page_tree is not None, 'page_tree cannot be none'

        # 获取分页控件对象集合
        pagination_tags = page_tree.xpath(test_pagination_tags_xpath)
        assert pagination_tags is not None, 'pagination_tags cannot be none'
        print(f'pagination_tags size = {len(pagination_tags)}')

        # 遍历分页标签对象集合,获取每一个分页标签对象的超链接地址
        for tag in pagination_tags:
            print(tag)
            print(type(tag))
            # get_text()
            # print(f'tag.get_text() = {tag.get_text()}')
            # outerText
            print(f'attribute outerText = {tag.get("outerText")}')
            # outerHTML
            print(f'attribute outerHTML = {tag.get("outerHTML")}')
            # data-page
            print(f'attribute data-page = {tag.get("data-page")}')
            # href
            print(f'attribute href = {tag.get("href")}')

    @staticmethod
    def doc_tree_example():
        # 获取测试博客文档页面的DOM树对象
        log.debug('invoke method -> doc_tree_example()')
        # 测试博客文档连接:test_doc_link
        response = requests.get(url=test_doc_link, headers=test_headers)
        page_context = response.text
        tree = etree.HTML(page_context)
        assert tree is not None, 'xml tree cannot be none'
        # print(type(tree))
        return tree

    @staticmethod
    def test_get_document_properties():
        # 测试获取文档对象的各个属性
        # 测试链接: https://blog.51cto.com/oldboy/1189530
        log.debug('invoke method -> test_get_document_properties()')

        # 获取测试博客文档的页面DOM对象
        page_tree = doc_tree_example()
        assert page_tree is not None, 'xml tree cannot be none'

        # 测试: 获取文档对象大标题 eg: LDAP跨多机房统一认证及授权管理精品解决方案
        title = page_tree.xpath(test_doc_title_xpath)
        assert title is not None, 'title cannot be none'
        title_text = title.get_text()
        print(f'doc_title = {title_text}')

        # 测试: 获取文档摘要内容

        # 测试: 获取文档正文内容

        # 测试: 获取完整文档的页面HTML页面

        # 测试: 获取文档的创建时间,文档的分类标签,分类类别名称
        pass

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    # test_suite.addTest(TestExamples('test_get_dom_tree'))  # test_get_dom_tree
    # test_suite.addTest(TestExamples('test_get_page_doc_list'))  # test_get_page_doc_list
    # test_suite.addTest(TestExamples('test_get_pagination_tags'))  # test_51cto_get_pagination_tags
    test_suite.addTest(TestExamples('test_get_document_properties'))  # test_get_document_properties
    runner = unittest.TextTestRunner()
