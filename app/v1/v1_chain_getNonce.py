#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getNonce.py
@time: 2020/1/8 5:23 下午
@desc:
'''
from flask import Blueprint
from app.src.chain_interface.chain_getNonce import *

chain_getNonce = Blueprint('chain_getNonce', __name__)


@chain_getNonce.route('/<api_name>/<params>')
def api_getNonce(api_name, params):
	"""
	查询地址在链上的nonce,chain_getNonce
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getNonce","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:chain_getNonce
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
           description: 待查询地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回链上nonce 200 OK
		"""
	result = getNonce(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "chain_getNonce"
	params = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	api_getNonce(api_name, params)


