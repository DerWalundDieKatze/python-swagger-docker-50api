#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_importKeyStore.py
@time: 2020/1/8 5:57 下午
@desc:
'''

from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_importKeyStore import *

account_importKeyStore = Blueprint('account_importKeyStore_keystore', __name__)


@account_importKeyStore.route('/<api_name>/<params>')
def api_importKeyStore(api_name, params):
	"""
	生成其他链的地址,account_importKeyStore
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_importKeyStore","params":["path","123"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:account_importKeyStore
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
           description:  params,必须为数组,eg.["path", "123"]
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = importKeyStore(api_name, params)
	return result




if __name__ == '__main__':
	api_name = "account_importKeyStore"
	params = ["path", "123"]
	api_importKeyStore(api_name, params)





