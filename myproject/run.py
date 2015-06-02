# -*- coding: utf-8 -*-
from app import app

if __name__ == '__main__':
    app.run(debug = True) # 设置调试模式，生产模式的时候要关掉debug
