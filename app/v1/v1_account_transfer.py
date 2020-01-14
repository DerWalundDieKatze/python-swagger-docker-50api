#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_transfer.py
@time: 2020/1/8 5:41 下午
@desc:
'''

from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_transfer import *

account_transfer = Blueprint('account_transfer_transaction', __name__)


@account_transfer.route('/<api_name>/<params>')
def api_transfer(api_name, params):
	"""
	account_transfer
	设置别名,account_transfer
       ---
       tags:
         - API_NAME:account_transfer
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
           description: 发起转账的地址；接受者的地址；金额；gas价格；gas上限；备注 ,必须为数组,
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回交易地址 200 OK
		"""
	result = transfer(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "account_transfer"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x111","0x110","0x30000",""]
	transfer(api_name, params)
	

