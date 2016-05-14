#!/usr/bin/env python
# coding: utf-8
# author: songjianhao
# e-mail: fredmail03@126.com
# Pw @ 2016-04-26 15:50

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from . import db,login_manager
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model,UserMixin):
    __tablename__ = 'loginuser'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(60),unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(60))
    role = db.Column(db.String(30))
    email = db.Column(db.String(60))
    telphone = db.Column(db.String(30))
    work_unit = db.Column(db.String(60))
    web_site = db.Column(db.String(70))

    def __repr__(self):
        return '<Role %r>' % self.role

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
