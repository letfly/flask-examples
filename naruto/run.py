#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'letfly'

# 导入Flask
from flask import Flask
# 导入sasuke中的create_app
from sasuke import create_app

# 初始化Flask放在sasuke里面通过create_app创建
app = create_app()

def main():
    # 设置服务器ip
    server_ip = '0.0.0.0'
    # 设置服务器端口
    server_port = 8000
    # 运行Flask
    app.run(host=server_ip, port=server_port, debug=True)

if __name__ == '__main__':
    main()
