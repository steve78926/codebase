#!/usr/bin/env python
# coding: utf-8
# author: songjianhao
# e-mail: fredmail03@126.com
# Pw @ 2016-04-26 15:50

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SelectField,SubmitField
from wtforms.validators import Required,Regexp,Length,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class RegisterForm(Form):
    username = StringField('用户名:',validators=[Required(),Length(1-64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9._]*$',0,
                                                          'Usernames must have only letters,'
                                                          'numbers, dot or underscores')])
    password_login = PasswordField('密码:',validators=[Required(),
                                                           EqualTo('password_vpn',
                                                                   message='密码必须匹配.')])
    password_vpn = PasswordField('确认密码:',validators=[Required()])
    name = StringField('姓名:',validators=[Required(),Length(1,60)])
    role = SelectField('角色:',choices =[('vpn','vpn'),('admin','admin')])
    email = StringField('邮箱',validators=[Required(),Length(1,60),Email()])
    submit = SubmitField('添加')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已经存在.')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已经存在.')

class MgmtChpasswdForm(Form):
    username = StringField('用户名:',validators=[Required(),
                                                   Length(1,64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9._]*$',0,
                                                          'Username must have only letter,'
                                                          'numbers,dot,understanders')])
    password_login = PasswordField('密码:',validators=[Required(),
                                                           EqualTo('password_vpn',
                                                                   message='密码不匹配')])
    password_vpn = PasswordField('确认密码：',validators=[Required()])
    submit = SubmitField('修改')

class FindUserForm(Form):
    username = StringField('用户名：',validators=[Required(),
                                              Length(1,64),Regexp('[A-Za-z][A-Za-z0-9._]*$',0,
                                                                  'Username must have only letter,'
                                                                  'numbers dot,nuderstanders')])
    submit = SubmitField('查询')



