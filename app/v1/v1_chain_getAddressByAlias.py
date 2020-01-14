#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getAddressByAlias.py
@time: 2020/1/8 5:27 下午
@desc:
'''

from flask import Blueprint
from app.src.chain_interface.chain_getAddressByAlias import *

chain_getAddressByAlias = Blueprint('chain_getAddressByAlias', __name__)


@chain_getAddressByAlias.route('/<api_name>/<params>')
def api_getAddressByAlias(api_name, params):
	"""
	根据别名获取别名对应的地址,chain_getAddressByAlias
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getAliasByAddress","params":["tom"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:
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
           description: 待查询地别名
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = getAddressByAlias(api_name, params)
	return result




if __name__ == '__main__':
	api_name = "chain_getAddressByAlias"
	params = ["tom"]
	api_getAddressByAlias(api_name, params)




