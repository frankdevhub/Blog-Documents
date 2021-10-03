#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：test_models_orm.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/9/4 17:15
"""

import logging as log
import unittest

from ..data.models import *
from ..data.sqlalchemy_orm import *

log.basicConfig(level=log.DEBUG)

class TestModelORM(unittest.TestCase):

    def test_get_session(self):
        log.debug('invoke method -> test_get_session()')
        session = get_session()
        log.debug(f'session = {session}')
        assert session is not None, f'session cannot be empty'

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestModelORM('test_get_session'))  # test_get_session
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
