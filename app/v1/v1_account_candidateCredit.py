#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_candidateCredit.py
@time: 2020/1/8 5:43 下午
@desc:
'''


from flask import Blueprint
from app.src.account_rpc_interface_account_manage.account_candidateCredit import *

account_candidateCredit = Blueprint('account_candidateCredit', __name__)


@account_candidateCredit.route('/<api_name>/<params>')
def api_candidateCredit(api_name, params):
	"""
	account_candidateCredit
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_candidateCredit","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x111","0x110","0x30000","{\"Pubkey\":\"0x020e233ebaed5ade5e48d7ee7a999e173df054321f4ddaebecdb61756f8a43e91c\",\"Node\":\"192.168.31.51:55555\"}"],"id":1}' http://127.0.0.1:15645
       ---
       tags:
         - API_NAME:创建账号
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
	result = candidateCredit(api_name, params)
	return result


if __name__ == '__main__':
	api_name = "account_candidateCredit"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "0x111", "0x110", "0x30000", "{\"Pubkey\":\"0x020e233ebaed5ade5e48d7ee7a999e173df054321f4ddaebecdb61756f8a43e91c\",\"Node\":\"192.168.31.51:55555\"}"]
	candidateCredit(api_name, params)

