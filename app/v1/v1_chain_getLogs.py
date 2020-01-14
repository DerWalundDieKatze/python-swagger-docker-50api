#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getLogs.py
@time: 2020/1/8 5:29 下午
@desc:
'''
from flask import Blueprint
from app.src.chain_interface.chain_getLogs import *

chain_getLogs = Blueprint('chain_getLogs', __name__)


@chain_getLogs.route('/<api_name>/<params>')
def api_getLogs(api_name, params):
	"""
	根据txhash获取交易log信息,chain_getLogs
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getLogs","params":["0x7d9dd32ca192e765ff2abd7c5f8931cc3f77f8f47d2d52170c7804c2ca2c5dd9"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:chain_getLogs
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
           description: 返回[]log 200 OK
		"""
	result = getLogs(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "chain_getLogs"
	params = ["0x7d9dd32ca192e765ff2abd7c5f8931cc3f77f8f47d2d52170c7804c2ca2c5dd9"]
	api_getLogs(api_name, params)





