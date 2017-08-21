#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifyEipAliasRequest(Request):

	def __init__(self):
		Request.__init__(self, 'eip', 'qcloudcliV1', 'ModifyEipAlias', 'eip.api.qcloud.com')

	def get_eipId(self):
		return self.get_params().get('eipId')

	def set_eipId(self, eipId):
		self.add_param('eipId', eipId)

	def get_eipName(self):
		return self.get_params().get('eipName')

	def set_eipName(self, eipName):
		self.add_param('eipName', eipName)

	def get_eipId(self):
		return self.get_params().get('eipId')

	def set_eipId(self, eipId):
		self.add_param('eipId', eipId)

	def get_eipName(self):
		return self.get_params().get('eipName')

	def set_eipName(self, eipName):
		self.add_param('eipName', eipName)

