#!/usr/bin/env python
# coding: utf-8
# author: songjianhao
# e-mail: fredmail03@126.com
# Pw @ 2016-04-26 15:50

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import flash,render_template,url_for,redirect
from . import mgmt
from .forms import RegisterForm,MgmtChpasswdForm,FindUserForm
from flask.ext.login import login_required
from ..models import User,db
from .. import mysql

@mgmt.route('/register',methods=['GET','POST'])
@login_required
def register():
    form = RegisterForm()
    cur = mysql.connect.cursor()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password_login.data,
                    email=form.email.data,
                    name=form.name.data,
                   role=form.role.data)
        db.session.add(user)
        db.session.commit()
        #print "passwod_vpn=%s" % form.password_vpn.data
        sql = "insert into user(username,password,name,email) VALUES ('%s',encrypt('%s'),'%s','%s')" % (form.username.data,form.password_login.data,form.name.data,form.email.data)
#        print "sql=%s" % sql
        cur.execute(sql)
        mysql.connect.commit()
        flash('您添加用户成功')
    return render_template('mgmt/register.html',form=form)

@mgmt.route('/adminHome')
@login_required
def adminHome():
    return render_template('mgmt/adminHome.html')

@mgmt.route('/mgmtchpasswd',methods=['GET','POST'])
@login_required
def mgmtChpasswd():
    form = MgmtChpasswdForm()
    cur = mysql.connect.cursor()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash("您输入的用户不存在")
            return redirect(url_for('.mgmtChpasswd'))
        user.password = form.password_login.data
        db.session.add(user)
        db.session.commit()
        sql = "update user set password = encrypt('%s') where username='%s'" % (form.password_login.data,form.username.data)
        #print "update sql = '%s'" % sql
        cur.execute(sql)
        flash("密码修改成功")
    return render_template('mgmt/mgmtChpasswd.html',form=form)

@mgmt.route('/FindUser',methods=['GET','POST'])
@login_required
def FindUser():
    form = FindUserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash("您输入的用户名不存在")
        else:
            userinfo = User.query.filter_by(username=form.username.data).all()
            return render_template('mgmt/FindUser.html',form=form,userinfo=userinfo)
    return render_template('mgmt/FindUser.html',form=form)

@mgmt.route('/select')
@login_required
def select():
    return render_template('mgmt/test.html')


