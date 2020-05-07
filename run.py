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

import dlib
from flask import Flask, template_rendered, render_template, request, redirect, url_for, jsonify
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
            data = {"filepath": filepath}
            # return render_template('show.html', filepath=filepath)
            detector = dlib.get_frontal_face_detector()
            predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

            # cv2读取图像
            img = cv2.imread('./static/'+filepath)

            # 取灰度
            img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

            # 人脸数rects
            rects = detector(img_gray, 0)
            print(len(rects))
            if len(rects) > 0:
                return jsonify(data)
            else:
                return "没有获取到人脸请重新上传"
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
    filepath = "./"+ path["path"]
    number = ocrIdCard(filepath, "522228199610032811")
    print(number)

    return {"data": number}


@app.route('/upload', methods=["GET"])
def upload():

    return render_template("upload.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
