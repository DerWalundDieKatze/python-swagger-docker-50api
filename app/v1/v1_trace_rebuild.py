#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_trace_rebuild.py
@time: 2020/1/8 5:36 下午
@desc:
'''



from flask import Blueprint
from app.src.recording_interface.trace_rebuild import *

trace_rebuild = Blueprint('trace_rebuild', __name__)


@trace_rebuild.route('/<api_name>/<params>')
def api_rebuild(api_name, params):
	"""
	重建trace中的区块记录,trace_rebuild
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_rebuild","params":[1,10], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:trace_rebuild
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
           description:  params,必须为数组
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description: 返回200 OK
		"""
	result = rebuild(api_name, params)
	return result


if __name__ == '__main__':
	api_name = "trace_rebuild"
	params = [1, 10]
	rebuild(api_name, params)
