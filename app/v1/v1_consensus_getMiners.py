#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_consensus_getMiners.py
@time: 2020/1/14 3:02 下午
@desc:
'''
from flask import Blueprint
from app.src.block.consensus_getMiners import *

consensus_getMiners = Blueprint('consensus_getMiners_Miners', __name__)


@consensus_getMiners.route('/<api_name>/<params>')
def api_getMiners(api_name, params):
	"""
	获取当前可以出块的节点
	curl http://local5645 -X POST --data '{"jsonrpc":"2.0","method":"consensus_getMiners","params":[""], "id": 3}' -H "Content-Type:application/json"host:1
	
       ---
       tags:
         - API_NAME:consensus_getMiners
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
           description: 返回私钥 200 OK
		"""
	result = getMiners(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "consensus_getMiners"
	params = [""]
	api_getMiners(api_name, params)
