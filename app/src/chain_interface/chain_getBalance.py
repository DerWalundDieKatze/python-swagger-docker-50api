#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getBalance.py
@time: 2020/1/8 5:22 下午
@desc:
'''

from app.src.API import request_Api

'''3. chain_getBalance'''


def getBalance(api_name, params):
	'''
	查询地址余额
	:param api_name: chain_getAliasByAddress
	:param params:待查询地址
	:return: 地址中的账号余额
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getBalance","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("查询地址余额成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("查询地址余额失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getBalance"
	params = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	getBalance(api_name, params)
