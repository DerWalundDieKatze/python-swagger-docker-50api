#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_listAddress.py
@time: 2020/1/8 5:38 下午
@desc:
'''

from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_listAddress import *

account_listAddress = Blueprint('account_call', __name__)


@account_listAddress.route('/<api_name>/<params>')
def api_listAddress(api_name, params):
	"""
	列出所有本地地址,account_listAddress
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_listAddress","params":[], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:account_listAddress
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
           description:  params,必须为数组,drep地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = listAddress(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "account_listAddress"
	params = []
	api_listAddress(api_name, params)




