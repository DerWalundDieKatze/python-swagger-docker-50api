#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getCancelCreditDetails.py
@time: 2020/1/8 5:30 下午
@desc:
'''


from flask import Blueprint
from app.src.chain_interface.chain_getCancelCreditDetails import *

chain_getCancelCreditDetails = Blueprint('chain_getCancelCreditDetails', __name__)


@chain_getCancelCreditDetails.route('/<api_name>/<params>')
def api_getCancelCreditDetails(api_name, params):
	"""
	获取所有退票请求的细节,chain_getCancelCreditDetails
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getCancelCreditDetails","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:chain_getCancelCreditDetails
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
           description: 地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = getCancelCreditDetails(api_name, params)
	return result


if __name__ == '__main__':
	api_name = "chain_getCancelCreditDetails"
	params = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	api_getCancelCreditDetails(api_name, params)





