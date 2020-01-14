#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_log_setVmodule.py
@time: 2020/1/8 5:33 下午
@desc:
'''

from flask import Blueprint
from app.src.log.log_setVmodule import *

log_setVmodule = Blueprint('log_setVmodule', __name__)


@log_setVmodule.route('/<api_name>/<params>')
def api_setVmodule(api_name, params):
	"""
	分模块设置级别,log_setVmodule
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"log_setVmodule","params":["txpool=5"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:log_setVmodule
       parameters:
         - name: ""
           in: path
           type: string
           required: true
           description: api_name
           value: 1
         - name:
           in: path
           type: []
           description: 地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回bytecode 200 OK
		"""
	result = setVmodule(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "log_setVmodule"
	params = ["txpool=5"]
	api_setVmodule(api_name, params)





