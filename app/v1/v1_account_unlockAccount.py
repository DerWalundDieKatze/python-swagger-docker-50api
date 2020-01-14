#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_unlockAccount.py
@time: 2020/1/8 5:40 下午
@desc:
'''

from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_unlockAccount import *

account_unlockAccount = Blueprint('account_unlockAccount', __name__)


@account_unlockAccount.route('/<api_name>/<params>')
def api_unlockAccount(api_name, params):
	"""
	account_unlockAccount
	账号地址,account_unlockAccount
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
           description:  params,必须为数组,
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回失败返回错误原因，成功不返回任何信息 200 OK
		"""
	result = unlockAccount(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "account_unlockAccount"
	params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"]
	api_unlockAccount(api_name, params)



