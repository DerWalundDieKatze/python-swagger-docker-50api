#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_candidateCredit.py
@time: 2020/1/8 5:43 下午
@desc:
'''


from app.src.API import request_Api

'''12. account_CandidateCredit'''


def candidateCredit(api_name, params):
	'''
	候选投票
	:param api_name: "trace_decodeTrasnaction"
	:param params: 发起转账的地址；接受者的地址；金额；gas价格；gas上线；用户pubkey ip等信息
	:return: 交易地址
	示例代码
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_candidateCredit","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x111","0x110","0x30000","{\"Pubkey\":\"0x020e233ebaed5ade5e48d7ee7a999e173df054321f4ddaebecdb61756f8a43e91c\",\"Node\":\"192.168.31.51:55555\"}"],"id":1}' http://127.0.0.1:15645
	'''
	try:
		result = request_Api(api_name, params)
		print("候选投票成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("候选投票失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_candidateCredit"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "0x111", "0x110", "0x30000", "{\"Pubkey\":\"0x020e233ebaed5ade5e48d7ee7a999e173df054321f4ddaebecdb61756f8a43e91c\",\"Node\":\"192.168.31.51:55555\"}"]
	candidateCredit(api_name, params)
