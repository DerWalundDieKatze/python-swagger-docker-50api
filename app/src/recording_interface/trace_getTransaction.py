#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_trace_getTransaction.py
@time: 2020/1/8 5:35 下午
@desc:
'''

import logging

from app.src.API import request_Api

'''2. trace_getTransaction'''


def getTransaction(api_name, params):
	'''
	根据交易hash查询交易详细信息
	e.g:
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getTransaction","params":["0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"], "id": 3}' -H "Content-Type:application/json"
	:param api_name:
	:param params:  交易hash
	:return: 交易详细信息
	'''
	try:
		result = request_Api(api_name, params)
		print("根据交易hash查询交易详细信息成功，{}".format(result))
		return result
	except Exception as e:
		print("根据交易hash查询交易详细信息,api返回错误".format(e))
		logging.info("根据交易hash查询交易详细信息,api返回错误".format(e))
		return -1


if __name__ == '__main__':
	api_name = "trace_getTransaction"
	params = ["0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"]
	getTransaction(api_name, params)
