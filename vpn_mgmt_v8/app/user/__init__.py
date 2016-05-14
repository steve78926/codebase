#!/usr/bin/env python
# coding: utf-8
# author: songjianhao
# e-mail: fredmail03@126.com
# Pw @ 2016-04-25 15:50

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Blueprint

user = Blueprint('user',__name__)

from . import views