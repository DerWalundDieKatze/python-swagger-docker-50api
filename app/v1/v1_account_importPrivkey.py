#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_importPrivkey.py
@time: 2020/1/8 5:58 下午
@desc:
'''

from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_importPrivkey import *

account_importPrivkey = Blueprint('account_importPrivkey_privkey', __name__)


@account_importPrivkey.route('/<api_name>/<params>')
def api_importPrivkey(api_name, params):
	"""
	导入私钥,account_importPrivkey
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_importPrivkey","params":["0xe5510b32854ca52e7d7d41bb3196fd426d551951e2fd5f6b559a62889d87926c"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:account_importPrivkey
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
           description:  params,必须为数组,eg.account_importPrivkey
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = importPrivkey(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "account_importPrivkey"
	params = ["0xe5510b32854ca52e7d7d41bb3196fd426d551951e2fd5f6b559a62889d87926c"]
	api_importPrivkey(api_name, params)






