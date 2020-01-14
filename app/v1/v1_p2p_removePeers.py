#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_p2p_removePeers.py
@time: 2020/1/8 5:33 下午
@desc:
'''

from flask import Blueprint
from app.src.p2p.p2p_removePeers import *

p2p_removePeers = Blueprint('p2p_removePeers', __name__)


@p2p_removePeers.route('/<api_name>/<params>')
def api_removePeers(api_name, params):
	"""
	移除节点,p2p_removePeers
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"p2p_removePeers","params":["enode://e1b2f83b7b0f5845cc74ca12bb40152e520842bbd0597b7770cb459bd40f109178811ebddd6d640100cdb9b661a3a43a9811d9fdc63770032a3f2524257fb62d@192.168.74.1:44444"]
], "id": 3}' -H "Content-Type:application/json"
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
           description: 地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回bytecode 200 OK
		"""
	result = removePeers(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "p2p_removePeers"
	params = [
		"enode://e1b2f83b7b0f5845cc74ca12bb40152e520842bbd0597b7770cb459bd40f109178811ebddd6d640100cdb9b661a3a43a9811d9fdc63770032a3f2524257fb62d@192.168.74.1:44444"]
	api_removePeers(api_name, params)




