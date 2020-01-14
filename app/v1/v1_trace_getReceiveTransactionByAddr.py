#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_trace_getReceiveTransactionByAddr.py
@time: 2020/1/8 5:36 下午
@desc:
'''

from flask import Blueprint
from app.src.recording_interface.trace_getReceiveTransactionByAddr import *

trace_getReceiveTransactionByAddr = Blueprint('trace_getReceiveTransactionByAddr', __name__)


@trace_getReceiveTransactionByAddr.route('/<api_name>/<params>')
def api_getReceiveTransactionByAd(api_name, params):
	"""
	根据地址查询该地址接受的交易，支持分页,trace_getReceiveTransactionByAddr
	'{"jsonrpc":"2.0","method":"trace_getReceiveTransactionByAddr","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5",1,10], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:trace_getReceiveTransactionByAddr
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
	result = getReceiveTransactionByAd(api_name, params)
	return result


if __name__ == '__main__':
	api_name = "trace_getReceiveTransactionByAddr"
	params = ["0x087adca1A1FCDCE8D21bcDe137e9ADCD66B282B0", 1, 10]
	getReceiveTransactionByAd(api_name, params)




