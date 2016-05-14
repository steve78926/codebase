#!/usr/bin/env python
# coding: utf-8
# author: songjianhao
# e-mail: fredmail03@126.com
# Pw @ 2016-04-25 15:50

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import render_template,flash
from flask.ext.login import current_user,login_required
from ..models import User,db
from . import user
from .forms import UserChpasswdForm
from .. import mysql

@user.route('/userChpasswd',methods=['GET','POST'])
@login_required
def user_Chpassword():
    form = UserChpasswdForm()
    cur = mysql.connect.cursor()
#    print "您当前的用户名: %s" % current_user.username
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password_login.data
            db.session.add(current_user)
            db.session.commit()
            sql = "update user set password=encrypt('%s') where username='%s'" % (form.password_login.data,current_user.username)
#            print "user_change_sql=%s" % sql
            cur.execute(sql)
            flash('密码修改成功,请点击"登出"返回主页面')
        else:
            flash('输入的老密码无效')
    return render_template('user/UserChangePassword.html',form=form)

@user.route('/userHome')
@login_required
def userHome():
    flash('密码修改成功')
    return render_template('user/userHome.html')


@user.route('/test')
def test():
    return render_template('/user/test.html')

