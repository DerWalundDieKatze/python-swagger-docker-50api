#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_blockmgr_getPoolTransactions.py
@time: 2020/1/8 5:18 下午
@desc:
'''

from flask import Blueprint
from app.src.block.blockmgr_getPoolTransactions import *

blockmgr_getPoolTransactions = Blueprint('blockmgr_getPoolTransactions', __name__)


@blockmgr_getPoolTransactions.route('/<api_name>/<params>')
def api_getPoolTransactions(api_name, params):
	"""
	获取交易池中的交易信息,blockmgr_getPoolTransactions
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"blockmgr_getPoolTransactions","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
       ---
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
           description: 待查询地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回交易池中所有交易 200 OK
		"""
	result = getPoolTransactions(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "blockmgr_getPoolTransactions"
	params = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	request_Api(api_name, params)



