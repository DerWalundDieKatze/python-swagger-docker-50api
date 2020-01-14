#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_openWallet.py
@time: 2020/1/8 5:40 下午
@desc:
'''

from app.src.API import request_Api


'''6. account_openWallet'''


def openWallet(api_name, params):
	'''
	打开钱包
	:param api_name: account_openWallet
	:param params:钱包密码
	:return: 无
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_openWallet","params":["123"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("打开钱包成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("打开钱包失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_openWallet"
	params = ["123"]
	openWallet(api_name, params)
