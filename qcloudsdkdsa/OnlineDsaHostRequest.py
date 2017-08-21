#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class OnlineDsaHostRequest(Request):

	def __init__(self):
		Request.__init__(self, 'dsa', 'qcloudcliV1', 'OnlineDsaHost', 'dsa.api.qcloud.com')

	def get_hostId(self):
		return self.get_params().get('hostId')

	def set_hostId(self, hostId):
		self.add_param('hostId', hostId)

