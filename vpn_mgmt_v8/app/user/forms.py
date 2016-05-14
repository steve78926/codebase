#!/usr/bin/env python
# coding: utf-8
# author: songjianhao
# e-mail: fredmail03@126.com
# Pw @ 2016-04-25 15:50

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,EqualTo,Regexp

class UserChpasswdForm(Form):
    old_password = PasswordField('老密码(清除自动添入的密码，手工输入):',validators=[Required()])
    password_login = PasswordField('新密码:',validators=[Required(),
                                                              EqualTo('password_vpn',
                                                                      message='密码必须匹配.')])
    password_vpn = PasswordField('修改密码:',validators=[Required()])
    submit = SubmitField('修改')