# -*- coding: utf-8 -*-
from flask import Flask # 引入Flas对象
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__) # 实例化一个flask对象
app.config.from_object('config') # 载入配置文件
db = SQLAlchemy(app) # 初始化db对象

# from app import views, models # 引用视图和模型
import views
