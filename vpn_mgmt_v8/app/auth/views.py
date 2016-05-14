#!/usr/bin/env python
# coding: utf-8
# author: songjianhao
# e-mail: fredmail03@126.com
# Pw @ 2016-04-26 15:50

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask.ext.login import login_user,logout_user,login_required
from flask import render_template,url_for,redirect,request,flash
from . import auth
from .forms import LoginForm
from ..models import User
from .. import mysql

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    cur = mysql.connect.cursor()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            print "form-username: %s" % form.username.data
            sql = "select role from loginuser where username='%s'" % (form.username.data)
            cur.execute(sql)
            role = cur.fetchone()
            if 'admin' in role:
                return redirect(request.args.get('next') or url_for('mgmt.register'))
            else:
                 return redirect(request.args.get('next') or url_for('user.user_Chpassword'))
        flash("输入的密码不正确")
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录.')
    return redirect(url_for('auth.login'))
