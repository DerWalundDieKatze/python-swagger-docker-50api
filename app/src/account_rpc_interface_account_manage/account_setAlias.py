#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_setAlias.py
@time: 2020/1/8 5:41 下午
@desc:
'''

from app.src.API import request_Api

'''9. account_setAlias'''


def setAlias(api_name, params):
	'''
	设置别名
	:param api_name: account_setAlias
	:param params:带设置别名的地址；别名；gas价格；gas上限
	:return: 交易地址
	示例代码
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_setAlias","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","AAAAA","0x110","0x30000"],"id":1}' http://127.0.0.1:15645
	'''
	
	try:
		result = request_Api(api_name, params)
		print("锁定账号成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("锁定账号失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_setAlias"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","AAAAA","0x110","0x30000"]
	setAlias(api_name, params)
