# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    :  2020/4/30 10:35
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""

import cv2
from pytesseract import pytesseract
from datetime import datetime
gray_img = 0


def images():
    start = datetime.now()
    image = cv2.imread(r"./images/5925826be9a2675546f7fdfe435d6df.jpg")


    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_output = cv2.Canny(gray_img, 100, 200, 3)

    # findContours(canny_output, contours, hireachy, RETR_TREE, CHAIN_APPROX_SIMPLE, Point(0, 0))
    result = pytesseract.image_to_string(gray_img, lang='chi_sim')
    end = datetime.now()
    print(result, end - start)

if __name__ == '__main__':
    images()