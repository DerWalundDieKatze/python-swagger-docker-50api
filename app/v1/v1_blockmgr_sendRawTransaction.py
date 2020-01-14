#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_blockmgr_sendRawTransaction.py
@time: 2020/1/8 5:18 下午
@desc:
'''

from flask import Blueprint
from app.src.block.blockmgr_sendRawTransaction import *

blockmgr_sendRawTransaction = Blueprint('blockmgr_sendRawTransaction_transaction', __name__)


@blockmgr_sendRawTransaction.route('/<api_name>/<params>')
def api_sendRawTransaction(api_name, params):
	"""
	发送已签名的交易,blockmgr_sendRawTransaction
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"blockmgr_sendRawTransaction","params":["0x40a287b6d30b05313131317a4120dd8c23c40910d038fa43b2f8932d3681cbe5ee3079b6e9de0bea6e8e6b2a867a561aa26e1cd6b62aa0422a043186b593b784bf80845c3fd5a7fbfe62e61d8564"], "id": 3}' -H "Content-Type:application/json"
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
           description:
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = sendRawTransaction(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "blockmgr_sendRawTransaction"
	params = ["0x40a287b6d30b05313131317a4120dd8c23c40910d038fa43b2f8932d3681cbe5ee3079b6e9de0bea6e8e6b2a867a561aa26e1cd6b62aa0422a043186b593b784bf80845c3fd5a7fbfe62e61d8564"]
	api_sendRawTransaction(api_name, params)





