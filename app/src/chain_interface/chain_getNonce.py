#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getNonce.py
@time: 2020/1/8 5:23 下午
@desc:
'''

from app.src.API import request_Api

'''4. chain_getNonce'''


def getNonce(api_name, params):
	'''
	查询地址在链上的nonce
	:param api_name: chain_getNonce
	:param params:待查询地址
	:return: 链上nonce
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getNonce","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("查询地址在链上的nonce成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("查询地址在链上的nonce失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getNonce"
	params = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	getNonce(api_name, params)
