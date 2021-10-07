#!/usr/bin/env python
# encoding: utf-8
# @author: frankdevhub
# @contact: frankdevhub@gmail.com
# @blog: http://blog.frankdevhub.site
# @file: test_regex_expression.py
# @time: 2021/2/13 12:24
# @desc: 解析匹配的正则表达式测试

import logging as log
import re
import unittest

log.basicConfig(level=log.DEBUG)

"""
51CTO博客站点文章链接提取文档唯一编号 
eg: 
   input = https://blog.51cto.com/oldboy/1926142 
   output = 1926142 
"""
BLOG_DOC_ID_REGEX = """
.*(?P<header>/http[s]{0,1}:\/\/([\w.]+\/?)\S*/)(?P<union_id>\/[0-9]{1,})$
"""
TEST_BLOG_DOC_LINK = "https://blog.51cto.com/oldboy/1926142"  # 测试博客网址链接(51CTO平台)
TEST_BLOG_DOC_LINKS = ["https://blog.51cto.com/oldboy/1926142", "https://blog.51cto.com/oldboy/1884326",
                       "https://blog.51cto.com/oldboy/1855640", "https://blog.51cto.com/oldboy/775056",
                       "https://blog.51cto.com/oldboy/1855461", "https://blog.51cto.com/oldboy/1911034"]


class TestRegexExpression(unittest.TestCase):

    @staticmethod
    def test_match_blog_union_id():
        """
        测试正则表达式匹配博客文章链接的唯一标识
        eg:
           input = "https://blog.51cto.com/oldboy/1189530"
           output = 1189530(文档唯一识别号)
        """
        log.debug('invoke method -> test_match_blog_union_id()')
        test_example = TEST_BLOG_DOC_LINK
        print(f'test_blog_doc_link: {test_example}')
        # matched = re.search(r'\/[0-9]{1,}$', test_example, re.M | re.I)
        matched = re.search(BLOG_DOC_ID_REGEX, test_example, re.M | re.I)
        if matched:
            print(f'result: {matched.group()}')
            # print(f'union_id: {matched.group("union_id")}')  # union_id
        else:
            print('result: not matched')

    @staticmethod
    def test_match_blog_union_ids():
        """测试逐个匹配51cto博客测试链接集合,匹配博文的唯一标识"""
        log.debug('invoke method -> test_match_blog_union_ids()')
        for link in TEST_BLOG_DOC_LINKS:
            print(link)
        pass


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(TestRegexExpression("test_match_blog_union_id"))  # test_match_blog_union_id
    # testunit.addTest(TestRegexExpression("test_match_blog_union_ids"))  # test_match_blog_union_ids
    runner = unittest.TextTestRunner()
    runner.run(testunit)
