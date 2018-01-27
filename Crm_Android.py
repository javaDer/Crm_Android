#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
from flask.ext.pymongo import PyMongo
from config import MongoDB
import chardet
import urllib

app = Flask(__name__)
# 实例化数据库配置，可以直接一行解决
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/v1/api/', methods=['GET', 'POST'])
def save():
    paramers = request.get_data()
    print (urllib.unquote(paramers))
    geographical = mongo.db.geographical
    geographical.insert({"username": "swper", "password": "123456"})
    if geographical:
        return "用户已经存在！"
    else:
        return "Added User!"


if __name__ == '__main__':
    app.run(host='192.168.1.4', port=5000)
