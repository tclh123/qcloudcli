#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CdbTdsqlGetOrderInfoRequest(Request):

	def __init__(self):
		Request.__init__(self, 'tdsql', 'qcloudcliV1', 'CdbTdsqlGetOrderInfo', 'tdsql.api.qcloud.com')

	def get_dealIds(self):
		return self.get_params().get('dealIds')

	def set_dealIds(self, dealIds):
		self.add_param('dealIds', dealIds)

