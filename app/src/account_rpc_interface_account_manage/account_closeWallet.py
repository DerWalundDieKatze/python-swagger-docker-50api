#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_closeWallet.py
@time: 2020/1/8 5:40 下午
@desc:
'''

from app.src.API import request_Api

'''7. account_closeWallet'''


def closeWallet(api_name, params):
	'''
	关闭钱包
	:param api_name: "account_closeWallet"
	:param params:
	:return: 无
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_closeWallet","params":[], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("关闭钱包成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("关闭钱包失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_closeWallet"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "0x111", "0x110", "0x30000", "{\"Pubkey\":\"0x020e233ebaed5ade5e48d7ee7a999e173df054321f4ddaebecdb61756f8a43e91c\",\"Node\":\"192.168.31.51:55555\"}"]
	closeWallet(api_name, params)