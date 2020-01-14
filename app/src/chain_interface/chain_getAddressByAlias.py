#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getAddressByAlias.py
@time: 2020/1/8 5:27 下午
@desc:
'''

from app.src.API import request_Api

'''8. chain_getAddressByAlias'''


def getAddressByAlias(api_name, params):
	'''
	根据别名获取别名对应的地址
	:param api_name: chain_getAddressByAlias
	:param params:待查询地别名
	:return: 别名对应的地址
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getAddressByAlias","params":["tom"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("根据别名获取别名对应的地址成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("根据别名获取别名对应的地址失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getAddressByAlias"
	params = ["tom"]
	getAddressByAlias(api_name, params)
