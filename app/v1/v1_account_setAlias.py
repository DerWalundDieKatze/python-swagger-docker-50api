#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_setAlias.py
@time: 2020/1/8 5:41 下午
@desc:
'''
from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_setAlias import *

account_setAlias = Blueprint('account_setAlias', __name__)


@account_setAlias.route('/<api_name>/<params>')
def api_setAlias(api_name, params):
	"""
	account_setAlias
	设置别名,account_setAlias
       ---
       tags:
         - API_NAME:account_setAlias
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
           description:  params,必须为数组,["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "AAAAA", "0x110", "0x30000"]
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回交易地址 200 OK
		"""
	result = setAlias(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "account_setAlias"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "AAAAA", "0x110", "0x30000"]
	api_setAlias(api_name, params)


