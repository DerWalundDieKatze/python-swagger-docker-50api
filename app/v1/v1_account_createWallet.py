#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_createWallet.py
@time: 2020/1/8 5:39 下午
@desc:
'''

from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_createAccount import *

account_createWallet = Blueprint('account_closeWallet', __name__)


@account_createWallet.route('/<api_name>/<params>')
def api_createWallet(api_name, params):
	"""
	创建本地钱包,account_createWallet
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_createWallet","params":["123"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:创建本地账号
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
	result = createAccount(api_name, params)
	return result


if __name__ == '__main__':
	api_name = "account_createWallet"
	params = ["123"]
	api_createWallet(api_name, params)






