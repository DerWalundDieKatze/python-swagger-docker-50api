#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_p2p_getPeers.py
@time: 2020/1/8 5:32 下午
@desc:
'''

from app.src.API import request_Api

'''p2p_getPeers'''


def getPeers(api_name, params):
	'''
	获取当前连接的节点
	:param api_name:p2p_getPeers
	:param params:空
	:return: p2p信息+ip地址
	示例代码
	curl http://127.0.0.1:15645 -X POST --data '{"jsonrpc":"2.0","method":"p2p_getPeers","params":"", "id": 3}' -H "Content-Type:application/json"
	响应：
	{"jsonrpc":"2.0","id":3,"result":[{},{},{},{}]}
	'''
	try:
		result = request_Api(api_name, params)
		#print("获取当前连接的节点，当前节点为：{}".format(result))
		return result
	except Exception as e:
		print("获取当前连接的节点api报错，{}".format(e))
		return -1
	finally:
		print("获取当前连接的节点，当前节点为：{}".format(result))


if __name__ == '__main__':
	api_name = "p2p_getPeers"
	params = ""
	getPeers(api_name, params)
