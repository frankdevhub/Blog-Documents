#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：constants.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/9/4 18:34
"""


class Xpath:
    """
      selenium dicts
      web element attribute name
      页面对象常用属性参数
    """
    ATTRIBUTE_NAME = "name"
    ATTRIBUTE_TITLE = "title"
    ATTRIBUTE_TARGET = "target"
    ATTRIBUTE_HREF = "href"
    ATTRIBUTE_CLASS = "class"
    ATTRIBUTE_VALUE = "value"


class WebLinks:
    """网络资源相关链接地址"""
    BAI_DU = "https://www.baidu.com"  # 百度首页地址
    BLOG_EXAMPLE_1 = "https://blog.51cto.com/oldboy"  # 51CTO博客站点实例(https://blog.51cto.com/oldboy)


class BusinessConstants:
    """业务常用字段"""
    # 接口规范常用字段
    SUCCESS = "success"  # 返回成功
    # selenium configuration
    SELENIUM_CACHE_ROOT_NULL = "selenium cache root directory path should not be null"  # 驱动缓存路径配置不存在
    SELENIUM_CACHE_ROOT_NOT_EXISTS = "selenium cache root directory not exist"  # 驱动缓存配置文件不存在
    SELENIUM_CACHE_FILE_NAME_NULL = "selenium cache file name should not be null"  # 驱动缓存路径配配置为空
    SELENIUM_WEB_DRIVER_PATH_NULL = "selenium web driver path should not be null"  # 无法加载驱动,路径配置为空
    SELENIUM_WEB_DRIVER_NOT_EXIST = "selenium web driver not exist"  # 无法加载驱动,驱动不存在
    # 字符信息常量
    CHARACTER_NULL_ARGUMENT = "character should not be null"  # 字符不能为空
    INVALID_CHINESE_CHARACTER = "not a chinese character"  # 非中文的字符异常
    INVALID_ENGLISH_CHARACTER = "not an english character"  # 非英文的字符的异常

#
# if __name__ == '__main__':
#     url_link = BusinessConstants.BLOG_EXAMPLE_1
#     print(url_link)
