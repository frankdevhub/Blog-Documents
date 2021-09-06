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

"""企业岗位招聘人数的正则表达式 eg:(招1人)"""
HEAD_COUNT_REGEX = """
.*(?P<prefix>[招聘|招纳|招|需要|急需|需]+)(?P<numeric>[\u4e00-\u9fa5\u767e\u5343\u96f6]+|[0-9]+|[若干])(?P<surfix>人)$
"""
TEST_HEAD_COUNT = "招 23 人"
"""
51CTO博客站点文章链接提取文档唯一编号 
eg: 
   input = https://blog.51cto.com/oldboy/1926142 
   output = 1926142 
"""
BLOG_DOC_ID_REGEX = """sss"""
TEST_BLOG_DOC_LINK = "https://blog.51cto.com/oldboy/1926142"
TEST_BLOG_DOC_LINKS = ["https://blog.51cto.com/oldboy/1926142", "https://blog.51cto.com/oldboy/1884326",
                       "https://blog.51cto.com/oldboy/1855640", "https://blog.51cto.com/oldboy/775056",
                       "https://blog.51cto.com/oldboy/1855461", "https://blog.51cto.com/oldboy/1911034"]


class TestRegexExpression(unittest.TestCase):

    @staticmethod
    def test_match_head_count():
        """
        测试正则表达式匹配企业招聘预算人数
        eg:
           input = "本季度企业预计招聘23人,其中应届毕业生预计招收12人"
           output = 23, 12
        """
        log.debug('invoke method -> test_match_head_count()')
        matched = re.match(HEAD_COUNT_REGEX, TEST_HEAD_COUNT, re.M | re.I)
        if matched:
            print("prefix :", matched.group('prefix'))
        else:
            print('no matched')

    @staticmethod
    def test_match_blog_union_id():
        log.debug('invoke method -> test_match_blog_union_id()')

    pass


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.add(TestRegexExpression("test_match_head_count"))  # test_match_head_count
    testunit.add(TestRegexExpression("test_match_blog_union_id"))  # test_match_blog_union_id
    runner = unittest.TextTestRunner()
    runner.run(testunit)
