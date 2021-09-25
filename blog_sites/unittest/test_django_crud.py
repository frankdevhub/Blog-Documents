# !/usr/bin/env python
# encoding: utf-8
# @author: frankdevhub
# @contact: frankdevhub@gmail.com
# @blog: http://blog.frankdevhub.site
# @file: test_django_crud.py
# @time: 2021/2/16 12:03

import logging as log
import os
import unittest

import django

from ..models.models import BlogDocumentBrief

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frankdevhub_blog_documents.settings')
django.setup()

log.basicConfig(level=log.DEBUG)


class DjangoCrudTest(unittest.TestCase):

    @staticmethod
    def test_insert():
        log.debug('invoke method -> test_insert()')
        obj = BlogDocumentBrief('', 'blog_domain', 'doc_title')
        obj.save()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(DjangoCrudTest("test_insert"))  # test_insert
    runner = unittest.TextTestRunner()
    runner.run(testunit)
