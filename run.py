# -*- encoding: utf-8 -*-
"""
@File    : run.py
@Time    :  2020/4/29 9:07
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import time
from datetime import datetime
from flask import Flask, template_rendered, render_template, request, redirect, url_for
import numpy as np
import cv2
import os

from identity import ocrIdCard

app = Flask(__name__)

UPLOAD_FOLDER = '/path/to/the/uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])


@app.route('/', methods=["POST"])
def hello_world():
    file = request.files.get('img')
    if file:
        path = os.getcwd()

        suffix = file.filename.rsplit(".")[1]
        if suffix in ALLOWED_EXTENSIONS:
            filepath = os.path.join(path, "images", str(int(time.time())) + "." + suffix)

            file.save(filepath)
            number = ocrIdCard('images/' + str(int(time.time())) + "." + suffix, "522228199610032811")
            data = {"number": number}
            return data
        else:
            return "暂时不能识别此图片类型"
    else:
        return "文件不能为空"


@app.route("/save", methods=["POST"])
def savefile():
    file = request.files.get('file')
    if file:
        path = os.getcwd()

        suffix = file.filename.rsplit(".")[1]
        if suffix in ALLOWED_EXTENSIONS:
            filename = str(int(time.time())) + "." + suffix
            filepath = os.path.join(path, "./static/images", filename)

            file.save(filepath)
            # number = ocrIdCard('./static/images/' + str(int(time.time())) + "." + suffix, "522228199610032811")
            # data = {"number": number}
            filepath = "images/" + filename
            return render_template('show.html', filepath=filepath)
        else:
            return "暂时不能识别此图片类型"
    else:
        return "文件不能为空"


@app.route('/index', methods=["GET"])
def index():

    return render_template("index.html")


@app.route('/show', methods=["GET"])
def show():

    return render_template("show.html")


@app.route('/discern', methods=["POST"])
def discern():
    path = request.form.to_dict()
    filepath = "."+ path["path"]
    number = ocrIdCard(filepath, "522228199610032811")
    print(number)
    return {"data": number}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)