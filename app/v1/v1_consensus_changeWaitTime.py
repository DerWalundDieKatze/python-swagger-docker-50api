#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_consensus_changeWaitTime.py
@time: 2020/1/8 5:58 下午
@desc:
'''
from flask import Blueprint
from app.src.consensus.consensus_changeWaitTime import *

consensus_changeWaitTime = Blueprint('account_sign', __name__)


@consensus_changeWaitTime.route('/<api_name>/<params>')
def api_changeWaitTime(api_name, params):
	"""
	修改leader等待时间 (ms);共识时间，一般救急时使用,consensus_changeWaitTime
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"consensus_changeWaitTime","params":[100000], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:consensus_changeWaitTime
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
           description: 等待时间(ms)
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回私钥 200 OK
		"""
	result = changeWaitTime(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "consensus_changeWaitTime"
	params = [100000]
	api_changeWaitTime(api_name, params)



