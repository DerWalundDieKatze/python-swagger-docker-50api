#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_blockmgr_getTxInPool.py
@time: 2020/1/8 5:20 下午
@desc:
'''

from flask import Blueprint
from app.src.block.blockmgr_getTxInPool import *

blockmgr_getTxInPool = Blueprint('blockmgr_getTxInPool', __name__)


@blockmgr_getTxInPool.route('/<api_name>/<params>')
def api_getTxInPool(api_name, params):
	"""
	查询交易是否在交易池，如果在，返回交易,blockmgr_getTxInPool
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"blockmgr_getTxInPool","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5"],"id":1}' http://127.0.0.1:15645
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
           description: 发起转账的地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = getTxInPool(api_name, params)
	return result




if __name__ == '__main__':
	api_name = "blockmgr_getTxInPool"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5"]
	api_getTxInPool(api_name, params)




