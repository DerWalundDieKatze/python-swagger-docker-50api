#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: consensus_getMiners.py
@time: 2020/1/14 2:27 下午
@desc:
'''

from app.src.API import request_Api

''' consensus_getMiners'''


def getMiners(api_name, params):
	'''
	获取当前可以出块的节点
	:param api_name: consensus_getMiners
	:param params:[""]
	:return:
	示例代码
	curl http://local5645 -X POST --data '{"jsonrpc":"2.0","method":"consensus_getMiners","params":[""], "id": 3}' -H "Content-Type:application/json"host:1
	'''
	try:
		result = request_Api(api_name, params)
		result = result["result"]
		print("获取当前可以出块的节点{}".format(result))
		return result
	except Exception as e:
		print("获取当前可以出块的节点接口报错,{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "consensus_getMiners"
	params = [""]
	getMiners(api_name, params)
