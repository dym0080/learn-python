# -*- coding: utf-8 -*-

# 使用flask框架

from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def sign_form():
     return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='123':
        return render_template('singin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password',username=username)

if __name__ == '__main__':
    app.run()
