# -*- coding: utf-8 -*-
from flask import Blueprint

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return 'frontend'


@frontend.route('/test/')
def test():
    return '/test/'
