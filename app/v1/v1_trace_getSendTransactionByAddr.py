#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_trace_getSendTransactionByAddr.py
@time: 2020/1/8 5:35 下午
@desc:
'''

from flask import Blueprint
from app.src.recording_interface.trace_getSendTransactionByAddr import *

trace_getSendTransactionByAddr = Blueprint('api_createAccount', __name__)


@trace_getSendTransactionByAddr.route('/<api_name>/<params>')
def api_getSendTransactionByAddr(api_name, params):
	"""
	根据地址查询该地址发出的交易，支持分页,trace_getSendTransactionByAddr
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getSendTransactionByAddr","params":["0x7923a30bbfbcb998a6534d56b313e68c8e0c594a",1,10], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:创建账号
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
	result = getSendTransactionByAddr(api_name, params)
	return result


if __name__ == '__main__':
	api_name = "trace_getSendTransactionByAddr"
	params = ["0x7923a30bbfbcb998a6534d56b313e68c8e0c594a", 1, 10]
	api_getSendTransactionByAddr(api_name, params)
