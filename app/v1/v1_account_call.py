#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_call.py
@time: 2020/1/10 6:05 下午
@desc:
'''

from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_call import call

account_call = Blueprint('account_call_call', __name__)


@account_call.route('/<api_name>/<params>')
def api_call(api_name, params):
	"""
	account_call
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_createCode","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x6d4ce63c","0x111","0x110","0x30000"],"id":1}' http://127.0.0.1:15645
       ---
       tags:
         - API_NAME:account_call
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
           description:  params,必须为数组;eg. []
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = call(api_name, params)
	return result


if __name__ == '__main__':
	api_name = "account_call"
	params = []
	result = call(api_name, params)
