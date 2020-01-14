#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_trace_decodeTrasnaction.py
@time: 2020/1/8 5:35 下午
@desc:
'''

from flask import Blueprint
from app.src.recording_interface.trace_decodeTrasnaction import *

trace_decodeTrasnaction = Blueprint('trace_decodeTrasnaction', __name__)


@trace_decodeTrasnaction.route('/<api_name>/<params>')
def api_decodeTrasnaction(api_name, params):
	"""
	把交易字节信息反解析成交易详情,trace_decodeTrasnaction
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_decodeTrasnaction","params":["0x02a7ae20007923a30bbfbcb998a6534d56b313e68c8e0c594a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002011102011003030000bc9889d00b004120eba14c77eab7a154833ff14832d8769cfc0b30db288445d6a83ef2fe337aa09042f8174a593543c4acabe7fadf1ad5fceea9c835682cb9dbea3f1d8fec181fb9"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:trace_decodeTrasnaction
       parameters:
         - name: ""
           in: path
           type: string
           required: true
           description: api_name
           value: 1
         - name:
           in: path
           type: []
           description: 交易字节信息
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回交易详情 200 OK
		"""
	result = decodeTrasnaction(api_name, params)
	return result




if __name__ == '__main__':
	api_name = "trace_decodeTrasnaction"
	params = [
		"0x02a7ae20007923a30bbfbcb998a6534d56b313e68c8e0c594a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002011102011003030000bc9889d00b004120eba14c77eab7a154833ff14832d8769cfc0b30db288445d6a83ef2fe337aa09042f8174a593543c4acabe7fadf1ad5fceea9c835682cb9dbea3f1d8fec181fb9"]
	api_decodeTrasnaction(api_name, params)




