#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_log_setLevel.py
@time: 2020/1/8 5:33 下午
@desc:
'''

from flask import Blueprint
from app.src.log.log_setLevel import *

log_setLevel = Blueprint('log_setLevel', __name__)


@log_setLevel.route('/<api_name>/<params>')
def api_setLevel(api_name, params):
	"""
	设置日志级别,log_setLevel
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"log_setLevel","params":["trace"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:chain_getByteCode
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
           description: 日志级别（"debug","0"）
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回bytecode 200 OK
		"""
	result = setLevel(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "log_setLevel"
	params = ["trace"]
	api_setLevel(api_name, params)






