#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_p2p_localNode.py
@time: 2020/1/9 11:43 上午
@desc:
'''
from flask import Blueprint
from app.src.p2p.p2p_localNode import *

p2p_localNode = Blueprint('account_sign', __name__)


@p2p_localNode.route('/<api_name>/<params>')
def api_localNode(api_name, params):
	"""
	需要获取本地的enode，用于P2p链接,p2p_localNode
	curl http://127.0.0.1:15645 -X POST --data '{"jsonrpc":"2.0","method":"p2p_localNode","params":"", "id": 3}' -H "Content-Type:application/json"
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
           description: [""]
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回本地节点的enode 200 OK
		"""
	result = localNode(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "p2p_localNode"
	params = [""]
	api_localNode(api_name, params)







