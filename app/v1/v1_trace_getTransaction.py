#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_trace_getTransaction.py
@time: 2020/1/8 5:35 下午
@desc:
'''
from flask import Blueprint
from app.src.recording_interface.trace_getTransaction import *

trace_getTransaction = Blueprint('trace_getTransaction', __name__)


@trace_getTransaction.route('/<api_name>/<params>')
def api_getTransaction(api_name, params):
	"""
	根据交易hash查询交易详细信息,trace_getTransaction
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getTransaction","params":["0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:api_getTransaction
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
           description:  params,必须为数组
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = getTransaction(api_name, params)
	return result


if __name__ == '__main__':
	api_name = "trace_getTransaction"
	params = [1, 10]
	api_getTransaction(api_name, params)
