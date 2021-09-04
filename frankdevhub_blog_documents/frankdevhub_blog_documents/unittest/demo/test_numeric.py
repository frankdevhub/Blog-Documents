#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：test_numeric.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/2/19 19:06
"""
import inspect
import logging as log
import unittest

from frankdevhub_51job_api.tools.numeric import NumericUnit

log.basicConfig(level=log.DEBUG)


class TestNumericUnit(unittest.TestCase):

    def test_numeric_unit_members(self):
        log.debug('invoke method -> test_numeric_unit_members()')
        for instance in NumericUnit.__members__:
            log.debug(f'{instance}')
            for (type_name, obj) in inspect.getmembers(instance):
                log.debug(f'type_name: {type_name}, obj: {obj}')


if __name__ == '__main__':
    unittest.main()
