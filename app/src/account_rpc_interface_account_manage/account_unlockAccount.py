#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_unlockAccount.py
@time: 2020/1/8 5:40 下午
@desc:
'''

from app.src.API import request_Api

'''5. account_account_unlockAccount'''


def unlockAccount(api_name, params):
	'''
	解锁账号
	:param api_name: account_unlockAccount
	:param params:账号地址
	:return: 失败返回错误原因，成功不返回任何信息
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_unlockAccount","params":["0x518b3fefa3fb9a72753c6ad10a2b68cc034ec391"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("转账成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("转账失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_unlockAccount"
	params = ["0x518b3fefa3fb9a72753c6ad10a2b68cc034ec391"]
	unlockAccount(api_name, params)