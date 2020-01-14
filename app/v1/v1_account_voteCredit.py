#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_voteCredit.py
@time: 2020/1/8 5:42 下午
@desc:
'''


from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_voteCredit import *

account_voteCredit = Blueprint('account_voteCredit_creadit', __name__)


@account_voteCredit.route('/<api_name>/<params>')
def api_voteCredit(api_name, params):
	"""
	account_voteCredit
	设置别名,account_voteCredit
       ---
       tags:
         - API_NAME:account_voteCredit
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
           description: eg.["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "0x111", "0x110", "0x30000"]
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回交易地址 200 OK
		"""
	result = voteCredit(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "account_voteCredit"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "0x111", "0x110", "0x30000"]
	api_voteCredit(api_name, params)





