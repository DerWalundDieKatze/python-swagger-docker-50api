#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_blockmgr_getTransactionCount.py
@time: 2020/1/8 5:19 下午
@desc:
'''

from flask import Blueprint
from app.src.block.blockmgr_getTransactionCount import *

blockmgr_getTransactionCount = Blueprint('blockmgr_getTransactionCount', __name__)


@blockmgr_getTransactionCount.route('/<api_name>/<params>')
def api_getTransactionCount(api_name, params):
	"""
	获取地址发出的交易总数,blockmgr_getTransactionCount
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"blockmgr_getTransactionCount","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"       ---
       tags:
         - API_NAME:blockmgr_getPoolTransactions
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
           description: 查询地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回获取地址发出的交易总数 200 OK
		"""
	result = getTransactionCount(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "blockmgr_getTransactionCount"
	params = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	api_getTransactionCount(api_name, params)




