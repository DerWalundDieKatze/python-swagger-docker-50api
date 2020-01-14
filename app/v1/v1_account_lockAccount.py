#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_lockAccount.py
@time: 2020/1/8 5:39 下午
@desc:
'''

from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_lockAccount import *

account_lockAccount = Blueprint('account_lockAccount', __name__)


@account_lockAccount.route('/<api_name>/<params>')
def api_lockAccount(api_name, params):
	"""
	锁定账号,account_lockAccount
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_lockAccount","params":["0x518b3fefa3fb9a72753c6ad10a2b68cc034ec391"], "id": 3}' -H "Content-Type:application/json"
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
           description:  params,必须为数组,需要锁住的账号地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回失败返回错误原因，成功不返回任何信息 200 OK
		"""
	result = lockAccount(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "account_lockAccount"
	params = []
	api_lockAccount(api_name, params)
	

