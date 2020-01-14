#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getTransactionByBlockHeightAndIndex.py
@time: 2020/1/8 5:24 下午
@desc:
'''
from flask import Blueprint
from app.src.chain_interface.chain_getTransactionByBlockHeightAndIndex import *

chain_getTransactionByBlockHeightAndIndex = Blueprint('chain_getTransactionByBlockHeightAndIndex', __name__)


@chain_getTransactionByBlockHeightAndIndex.route('/<api_name>/<params>')
def api_getTransactionByBlockHeightAndIndex(api_name, params):
	"""
	获取区块中特定序列的交易,chain_getTransactionByBlockHeightAndIndex
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getTransactionByBlockHeightAndIndex","params":[10000,1], "id": 3}' -H "Content-Type:application/json"
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
           description: 区块高度;交易序列
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回交易信息 200 OK
		"""
	result = getTransactionByBlockHeightAndIndex(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "chain_getTransactionByBlockHeightAndIndex"
	params = [1, 1]
	api_getTransactionByBlockHeightAndIndex(api_name, params)






