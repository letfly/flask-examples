# -*- coding: utf-8 -*-
from flask import Flask
from views import frontend, admin

DEFAULT_APP_NAME = 'NARUTO'

DEFAULT_MODULES=(
    (frontend, ''),
    (admin, '/admin'),
)

def create_app():
    """创建、初始化app"""
    app = Flask(DEFAULT_APP_NAME)
    # 使用flask中的Blueprint设置站点模块
    setting_modules(app, DEFAULT_MODULES)
    return app

def setting_modules(app, modules):
    """注册Blueprint模块"""
    for module, url_prefix in modules:
	# 通过register_blueprint注册
	app.register_blueprint(module, url_prefix=url_prefix)
	'''通过传递两个参数register_blueprint方法注册Blueprint。根据传递过来的参数module是admin与frontend，而admin与frontend是已经定义好了的Blueprint对象。url_prefix为绑定的url路径'''
