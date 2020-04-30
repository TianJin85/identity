# -*- encoding: utf-8 -*-
"""
@File    : setup.py
@Time    :  2020/4/30 12:02
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
# file: setup.py
from distutils.core import setup
from Cython.Build import cythonize

setup(name='Hello world app',
      ext_modules=cythonize("hello1.pyx"))