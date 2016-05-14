#!/usr/bin/env python
# coding: utf-8
# author: songjianhao
# e-mail: fredmail03@126.com
# Pw @ 2016-04-26 15:50

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    username = StringField('用户名:',validators=[Required()])
    password = PasswordField('密码:',validators=[Required()])
    remember_me = BooleanField('请记住我')
    submit = SubmitField('登录')

