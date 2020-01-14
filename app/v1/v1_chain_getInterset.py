#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getInterset.py
@time: 2020/1/13 6:27 下午
@desc:
'''

from flask import Blueprint
from app.src.log.chain_getInterset import *

chain_getInterset = Blueprint('chain_getInterset_insterset', __name__)


@chain_getInterset.route('/<api_name>/<params>')
def api_chain_getInterset(api_name, params):
	"""
	根据txhash获取退质押或者投票利息信息,chain_getInterset
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getInterset","params":["0x7d9dd32ca192e765ff2abd7c5f8931cc3f77f8f47d2d52170c7804c2ca2c5dd9"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:chain_getInterset
       parameters:
         - name: ""
           in: path
           type: string
           required: true
           description:
           value: 1
         - name:
           in: path
           type: []
           description: txhash
           value: 2
       responses:
         500:
           description: 500表示服务器报错
         200:
           description:  {} 200 OK
		"""
	result = getInterset(api_name, params)
	return result




if __name__ == '__main__':
	api_name = "chain_getCandidateAddrs"
	params = [""]
	api_chain_getInterset(api_name, params)





