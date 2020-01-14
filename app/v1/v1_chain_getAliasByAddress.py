#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getAliasByAddress.py
@time: 2020/1/8 5:24 下午
@desc:
'''


from flask import Blueprint
from app.src.chain_interface.chain_getAliasByAddress import *

chain_getAliasByAddress = Blueprint('chain_getAliasByAddress', __name__)


@chain_getAliasByAddress.route('/<api_name>/<params>')
def api_getAliasByAddress(api_name, params):
	"""
	根据地址获取地址对应的别名,chain_getAliasByAddress
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getAliasByAddress","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"       ---
       tags:
         - API_NAME:chain_getAliasByAddress
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
           description: 地址别名
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = getAliasByAddress(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "chain_getAliasByAddress"
	params = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	request_Api(api_name, params)
