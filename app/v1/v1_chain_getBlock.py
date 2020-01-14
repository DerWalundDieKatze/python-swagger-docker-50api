#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getBlock.py
@time: 2020/1/8 5:22 下午
@desc:
'''

from flask import Blueprint
from app.src.chain_interface.chain_getBlock import *

chain_getblock = Blueprint('chain_getblock', __name__)


@chain_getblock.route('/<api_name>/<params>')
def api_getblock(api_name, params):
	"""
	用于获取区块信息,chain_getblock
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getBlock","params":[1], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:chain_getblock
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
           description: 当前区块高度
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = getBlock(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "chain_getBlock"
	params = [1]
	api_getblock(api_name, params)

