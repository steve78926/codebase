#!/usr/bin/env python
# coding: utf-8
# author: songjianhao
# e-mail: fredmail03@126.com
# Pw @ 2016-04-26 15:50

import sys
reload(sys)
sys.setdefaultencoding('utf8')
class Config:
    SECRET_KEY = 'NO HARD TO GUESS'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://openvpn:1qaz2wsx!@#@127.0.0.1/openvpn'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'openvpn'
    MYSQL_PASSWORD = '1qaz2wsx!@#'
    MYSQL_DB = 'openvpn'

class ProductConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://openvpn:123456@127.0.0.1/openvpn'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'openvpn'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'openvpn'

config = {'develop': DevelopConfig,
          'product': ProductConfig,
          'default': DevelopConfig
          }

