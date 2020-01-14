#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getMaxHeight.py
@time: 2020/1/8 5:22 下午
@desc:
'''


from flask import Blueprint
from app.src.chain_interface.chain_getMaxHeight import *

chain_getMaxHeight = Blueprint('chain_getMaxHeight', __name__)


@chain_getMaxHeight.route('/<api_name>/<params>')
def api_getMaxHeight(api_name, params):
	"""
	用于获取当前最高区块,chain_getMaxHeight
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getMaxHeight","params":[], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:chain_getMaxHeight
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
           description: 返回当前最高区块高度数值 200 OK
		"""
	result = getMaxHeight(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "chain_getMaxHeight"
	params = []
	api_getMaxHeight(api_name, params)



