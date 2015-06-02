# -*- coding: utf-8 -*-
from flask import Flask # 引入Flas对象

app = Flask(__name__) # 实例化一个flask对象

import views # 导入views模块
