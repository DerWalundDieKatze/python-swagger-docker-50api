#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getReceipt.py
@time: 2020/1/8 5:28 下午
@desc:
'''

from flask import Blueprint
from app.src.chain_interface.chain_getReceipt import *

chain_getReceipt = Blueprint('chain_getReceipt', __name__)


@chain_getReceipt.route('/<api_name>/<params>')
def api_getReceipt(api_name, params):
	"""
	根据txhash获取receipt信息,chain_getByteCode
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getByteCode","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:chain_getByteCode
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
           description: txhash
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回receipt 200 OK
		"""
	result = getReceipt(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "chain_getReceipt"
	params = ["0x7d9dd32ca192e765ff2abd7c5f8931cc3f77f8f47d2d52170c7804c2ca2c5dd9"]
	api_getReceipt(api_name, params)





