#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getCreditDetails.py
@time: 2020/1/8 5:30 下午
@desc:
'''

from app.src.API import request_Api

'''12. chain_getCreditDetails'''


def getCreditDetails(api_name, params):
	'''
	根据地址获取stake 所有细节信息
	:param api_name: chain_getTransactionByBlockHeightAndIndex
	:param params:地址
	:return: bytecode
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getVoteCreditDetails","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("根据地址获取stake 所有细节信息，{}".format(result))
		return result
	except Exception as e:
		print("根据地址获取stake 所有细节信息失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getCreditDetails"
	params = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	getCreditDetails(api_name, params)
