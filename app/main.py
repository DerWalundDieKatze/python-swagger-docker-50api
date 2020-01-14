import sys

from app.v1.v1_account_call import *
from app.v1.v1_account_cancelVoteCredit import account_CancelVoteCredit
from app.v1.v1_account_closeWallet import account_closeWallet
from app.v1.v1_account_createCode import account_createCode
from app.v1.v1_account_createWallet import account_createWallet
from app.v1.v1_account_generateAddresses import account_generateAddresses
from app.v1.v1_account_importKeyStore import account_importKeyStore
from app.v1.v1_account_importPrivkey import account_importPrivkey
from app.v1.v1_account_listAddress import account_listAddress
from app.v1.v1_account_lockAccount import account_lockAccount
from app.v1.v1_account_openWallet import account_openWallet
from app.v1.v1_account_setAlias import account_setAlias
from app.v1.v1_account_sign import account_sign
from app.v1.v1_account_transfer import account_transfer
from app.v1.v1_account_unlockAccount import account_unlockAccount
from app.v1.v1_account_voteCredit import account_voteCredit
from app.v1.v1_blockmgr_getPoolTransactions import blockmgr_getPoolTransactions
from app.v1.v1_blockmgr_getTransactionCount import blockmgr_getTransactionCount
from app.v1.v1_blockmgr_getTxInPool import blockmgr_getTxInPool
from app.v1.v1_blockmgr_sendRawTransaction import blockmgr_sendRawTransaction
from app.v1.v1_chain_getAddressByAlias import chain_getAddressByAlias
from app.v1.v1_chain_getAliasByAddress import chain_getAliasByAddress
from app.v1.v1_chain_getBalance import chain_getBalance
from app.v1.v1_chain_getBlock import chain_getblock
from app.v1.v1_chain_getByteCode import chain_getByteCode
from app.v1.v1_chain_getCancelCreditDetails import chain_getCancelCreditDetails
from app.v1.v1_chain_getCandidateAddrs import chain_getCandidateAddrs
from app.v1.v1_chain_getCreditDetails import chain_getCreditDetails
from app.v1.v1_chain_getLogs import chain_getLogs
from app.v1.v1_chain_getMaxHeight import chain_getMaxHeight
from app.v1.v1_chain_getNonce import chain_getNonce
from app.v1.v1_chain_getReceipt import chain_getReceipt
from app.v1.v1_chain_getReputation import chain_getReputation
from app.v1.v1_chain_getTransactionByBlockHeightAndIndex import chain_getTransactionByBlockHeightAndIndex
from app.v1.v1_consensus_changeWaitTime import consensus_changeWaitTime
from app.v1.v1_log_setLevel import log_setLevel
from app.v1.v1_log_setVmodule import log_setVmodule
from app.v1.v1_p2p_addPeers import p2p_addPeers
from app.v1.v1_p2p_getPeers import p2p_getPeers
from app.v1.v1_p2p_removePeers import p2p_removePeers
from app.v1.v1_trace_decodeTrasnaction import trace_decodeTrasnaction
from app.v1.v1_trace_getRawTransaction import trace_getRawTransaction
from app.v1.v1_trace_getReceiveTransactionByAddr import trace_getReceiveTransactionByAddr
from app.v1.v1_trace_getSendTransactionByAddr import trace_getSendTransactionByAddr
from app.v1.v1_trace_getTransaction import trace_getTransaction
from app.v1.v1_trace_rebuild import trace_rebuild

sys.path.append('../')  # 新加入的
sys.path.append('.')  # 新加入的
from flasgger import Swagger
from flask import Flask

app = Flask(__name__)

# API 文档的配置
template = {
  "swagger": "2.0",
  "info": {
    "title": "50个API",
    "description": "在线API 调用测试",
    "contact": {
      "responsibleOrganization": "AturX",
      "responsibleDeveloper": "AturX",
      "email": "caroline.fang.cc@gmail.com",
      "url": "www.me.com",
    },
    "termsOfService": "http://me.com/terms",
    "version": "0.0.1"
  },
  "host": "192.168.31.146:5000",  # overrides localhost:5000
  "basePath": "/",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"
}
Swagger(app, template=template)



# 注册蓝图，并指定其对应的前缀（url_prefix）
'''区块 用于处理区块链偏上层逻辑'''
app.register_blueprint(blockmgr_sendRawTransaction, url_prefix="/blockmgr_sendRawTransaction_send")
app.register_blueprint(blockmgr_getPoolTransactions, url_prefix="/blockmgr_getPoolTransactions_get")
app.register_blueprint(blockmgr_getTransactionCount, url_prefix="/blockmgr_getTransactionCount_num")
app.register_blueprint(blockmgr_getTxInPool, url_prefix="/blockmgr_getTxInPool_getTx")
'''链接口 用于获取区块信息'''
app.register_blueprint(chain_getblock, url_prefix="/chain_getblock_getblock")
app.register_blueprint(chain_getMaxHeight, url_prefix="/chain_getMaxHeight_max_height")
app.register_blueprint(chain_getBalance, url_prefix="/chain_getBalance_balance")
app.register_blueprint(chain_getNonce, url_prefix="/chain_getNonce_nonce")
app.register_blueprint(chain_getReputation, url_prefix="/chain_getReputation_reputation")
app.register_blueprint(chain_getTransactionByBlockHeightAndIndex, url_prefix="/chain_getTransactionByBlockHeightAndIndex_HeightAndIndex")
app.register_blueprint(chain_getAliasByAddress, url_prefix="/chain_getAliasByAddress_alias_byaddress")
app.register_blueprint(chain_getAddressByAlias, url_prefix="/chain_getAddressByAlias_address_alia")
app.register_blueprint(chain_getReceipt, url_prefix="/chain_getReceipt_receipt")
app.register_blueprint(chain_getLogs, url_prefix="/chain_getLogs_getlogs")
app.register_blueprint(chain_getByteCode, url_prefix="/chain_getByteCode_get_byte_code")
app.register_blueprint(chain_getCreditDetails, url_prefix="/chain_getCreditDetails_get_credit_details")
app.register_blueprint(chain_getCancelCreditDetails, url_prefix="/chain_GetCancelCreditDetails_get_cancel_credit_details")
app.register_blueprint(chain_getCandidateAddrs, url_prefix="/chain_GetCandidateAddrs_get_candidate_addrs")
'''p2p网络接口 设置查询网络状态'''
app.register_blueprint(p2p_getPeers, url_prefix="/p2p_getPeers_get_peers")
app.register_blueprint(p2p_addPeers, url_prefix="/p2p_addPeers_add_peers")
app.register_blueprint(p2p_removePeers, url_prefix="/p2p_removePeers_remove_peers")
'''日志rpc接口 设置日志级别'''
app.register_blueprint(log_setLevel, url_prefix="/log_setLevel_set_level")
app.register_blueprint(log_setVmodule, url_prefix="/log_setVmodule_set_vmodule")
'''记录接口 查询交易地址等信息（需要开启记录模块）'''
app.register_blueprint(trace_getRawTransaction, url_prefix="/trace_getRawTransaction_get_raw_transaction")
app.register_blueprint(trace_getTransaction, url_prefix="/trace_getTransaction_get_transaction")
app.register_blueprint(trace_decodeTrasnaction, url_prefix="/trace_decodeTrasnaction_decode_transaction")
app.register_blueprint(trace_getSendTransactionByAddr, url_prefix="/trace_getSendTransactionByAddr_get_send_transaction")
app.register_blueprint(trace_getReceiveTransactionByAddr, url_prefix="/trace_getReceiveTransactionByAd_get_receive_transaction")
app.register_blueprint(trace_rebuild, url_prefix="/trace_rebuild_rebuild")
'''账号rpc接口 地址管理及发起简单交易'''
app.register_blueprint(account_listAddress, url_prefix="/account_listAddress_list_address")
app.register_blueprint(account_createWallet, url_prefix="/account_createWallet_creat_wallet")
app.register_blueprint(account_lockAccount, url_prefix="/account_lockAccount_lock_account")
app.register_blueprint(account_unlockAccount, url_prefix="/account_account_unlockAccount_unlock_account")
app.register_blueprint(account_openWallet, url_prefix="/account_openWallet_open_wallet")
app.register_blueprint(account_closeWallet, url_prefix="/account_closeWallet_close_wallet")
app.register_blueprint(account_transfer, url_prefix="/account_transfer_transfer")
app.register_blueprint(account_setAlias, url_prefix="/account_setAlias_set_alias")
app.register_blueprint(account_voteCredit, url_prefix="/account_VoteCredit_vote_credit")
app.register_blueprint(account_CancelVoteCredit, url_prefix="/account_CancelVoteCredit_cancel_vote_credit")
app.register_blueprint(chain_getCandidateAddrs, url_prefix="/account_CandidateCredit_candidate_credit")
app.register_blueprint(chain_getCancelCreditDetails, url_prefix="/account_CancelCandidateCredit_cancel_candidate_credit")
app.register_blueprint(account_call, url_prefix="/account_call_transfer")
app.register_blueprint(blockmgr_sendRawTransaction, url_prefix="/blockmgr_getPoolTransactions_send")
app.register_blueprint(account_createCode, url_prefix="/account_createCode_create_code")
app.register_blueprint(account_sign, url_prefix="/account_sign_sign")
app.register_blueprint(account_generateAddresses, url_prefix="/account_generateAddresses_generate_addresses")
app.register_blueprint(account_importKeyStore, url_prefix="/account_importKeyStore_import_key_store")
app.register_blueprint(account_importPrivkey, url_prefix="/account_importPrivkey_import_privkey")
'''共识rpc接口 查询共识节点功能'''
app.register_blueprint(consensus_changeWaitTime, url_prefix="/consensus_changeWaitTime_change_wait_time")
'''新增api'''
app.register_blueprint(chain_getCandidateAddrs, url_prefix="/chain_getCandidateAddrs_get_candidate_addrs")







if __name__ == '__main__':
    # 访问API 接口地址 ：  http://localhost:5001/apidocs/
   app.run(host='192.168.31.148', port='5000')