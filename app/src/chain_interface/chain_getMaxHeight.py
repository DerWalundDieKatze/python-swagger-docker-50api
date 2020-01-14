#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getMaxHeight.py
@time: 2020/1/8 5:22 下午
@desc:
'''

from app.src.API import request_Api

'''2. chain_getMaxHeight'''


def getMaxHeight(api_name, params):
	'''
	用于获取当前最高区块
	:param api_name: chain_getMaxHeight
	:param params:无
	:return: 当前最高区块高度数值
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getMaxHeight","params":[], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("用于获取当前最高区块成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("用于获取当前最高区块失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getMaxHeight"
	params = []
	getMaxHeight(api_name, params)
