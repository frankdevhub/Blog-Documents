#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：models_orm.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/3/7 22:23
"""

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# Base.metadata.drop_all(engine)

# Base.metadata.create_all(engine)

def get_session():
    engine = db.create_engine('mysql+pymysql://roo:root@admin@127.0.0.1:3306/blog_sites')
    assert engine is not None, f'db engine cannot be empty'
    session = sessionmaker(bind=engine)
    return session
