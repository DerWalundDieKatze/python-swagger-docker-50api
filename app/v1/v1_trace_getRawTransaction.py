#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_trace_getRawTransaction.py
@time: 2020/1/8 5:34 下午
@desc:
'''

from flask import Blueprint
from app.src.recording_interface.trace_getRawTransaction import *

trace_getRawTransaction = Blueprint('trace_getRawTransaction', __name__)


@trace_getRawTransaction.route('/<api_name>/<params>')
def api_getRawTransaction(api_name, params):
	"""
	根据交易hash查询交易字节,chain_getByteCode
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getByteCode","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
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
           description: 交易hash
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回交易字节信息 200 OK
		"""
	result = getRawTransaction(api_name, params)
	return result




if __name__ == '__main__':
	api_name = "trace_getRawTransaction"
	params = ["0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"]
	api_getRawTransaction(api_name, params)



