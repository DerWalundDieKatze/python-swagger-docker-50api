#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_p2p_getPeers.py
@time: 2020/1/8 5:32 下午
@desc:
'''

from flask import Blueprint
from app.src.p2p.p2p_getPeer import *

p2p_getPeers = Blueprint('p2p_getPeers', __name__)


@p2p_getPeers.route('/<api_name>/<params>')
def api_getPeers(api_name, params):
	"""
	获取当前连接的节点,p2p_getPeers
	curl http://127.0.0.1:15645 -X POST --data '{"jsonrpc":"2.0","method":"p2p_getPeers","params":"", "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:p2p_getPeers
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
           description: 空
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: p2p信息+ip地址
		"""
	result = getPeers(api_name, params)
	return result




if __name__ == '__main__':
	api_name = "p2p_getPeers"
	params = ""
	api_getPeers(api_name, params)




