#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getBlock.py
@time: 2020/1/8 5:22 下午
@desc:
'''

from app.src.API import request_Api

'''1. chain_getblock'''


def getBlock(api_name, params):
	'''
	用于获取区块信息
	:param api_name: chain_getBlock
	:param params:height usage: 当前区块高度
	:return: 区块明细信息
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getBlock","params":[1], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("获取区块信息成功，高度为{}".format(result))
		return result
	except Exception as e:
		print("获取区块信息失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getBlock"
	params = [1]
	getBlock(api_name, params)
