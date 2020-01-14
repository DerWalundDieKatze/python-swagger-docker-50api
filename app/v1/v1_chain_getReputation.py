from flask import Blueprint
from app.src.chain_interface.chain_getReputation import *

chain_getReputation = Blueprint('chain_getReputation', __name__)


@chain_getReputation.route('/<api_name>/<params>')
def api_getReputation(api_name, params):
	"""
	查询地址的名誉值,chain_getReputation
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getReputation","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
       ---
       tags:
         - API_NAME:chain_getByteCode
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
           description: 待查询地址
           value: 2
       responses:
         500:
           description: 返回500表示服务器报错
         200:
           description:  返回地址对应的名誉值 200 OK
		"""
	result = getReputation(api_name, params)
	return result



if __name__ == '__main__':
	api_name = "chain_getReputation"
	params = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	api_getReputation(api_name, params)




