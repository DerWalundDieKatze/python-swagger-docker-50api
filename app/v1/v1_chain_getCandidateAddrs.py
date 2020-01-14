#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getCandidateAddrs.py
@time: 2020/1/8 5:31 下午
@desc:
'''


from flask import Blueprint
from app.src.chain_interface.chain_getCandidateAddrs import *

chain_getCandidateAddrs = Blueprint('chain_getCandidateAddrs_get_candidate_addrs', __name__)


@chain_getCandidateAddrs.route('/<api_name>/<params>')
def api_getCandidateAddrs(api_name, params):
	"""
	获取所有候选节点地址和对应的信任值,chain_getCandidateAddrs
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getCandidateAddrs","params":[""], "id": 3}' -H "Content-Type:application/json"
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
           description: 待查询地址
           value: 2
       responses:
         500:
           description: 500表示服务器报错
         200:
           description:  200 OK
		"""
	result = getCandidateAddrs(api_name, params)
	return result




if __name__ == '__main__':
	api_name = "chain_getCandidateAddrs"
	params = [""]
	api_getCandidateAddrs(api_name, params)


