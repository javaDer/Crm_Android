#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
# from flask.ext.pymongo import PyMongo
import urllib
import json
import datetime
import pymongo

app = Flask(__name__)
# 实例化数据库配置，可以直接一行解决
# mongo = PyMongo(app)
client = pymongo.MongoClient(host='localhost', port=27017)
collection = client.position.expire
collection.create_index([("time", pymongo.ASCENDING)], expireAfterSeconds=66)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/v1/api/', methods=['GET', 'POST'])
def save():
    paramers = request.get_data()
    data = urllib.unquote(paramers)
    insert_data = data.split("=")[1]
    _data = json.loads(insert_data)
    collection.insert({
        "latitude": _data['latitude'],
        "longitude": _data['longitude'],
        "moblie": _data['moblie'],
        "address": _data['address'],
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    })


@app.route("/v1/get")
def getcollection():
    results = collection.find({'moblie': '17693522393'})
    _result = json.dumps(str(results))
    print _result


if __name__ == '__main__':
    app.run(host='192.168.1.4', port=5000)
