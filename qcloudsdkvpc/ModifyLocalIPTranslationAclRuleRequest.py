#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifyLocalIPTranslationAclRuleRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'ModifyLocalIPTranslationAclRule', 'vpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_directConnectGatewayId(self):
		return self.get_params().get('directConnectGatewayId')

	def set_directConnectGatewayId(self, directConnectGatewayId):
		self.add_param('directConnectGatewayId', directConnectGatewayId)

	def get_originalIP(self):
		return self.get_params().get('originalIP')

	def set_originalIP(self, originalIP):
		self.add_param('originalIP', originalIP)

	def get_translationIP(self):
		return self.get_params().get('translationIP')

	def set_translationIP(self, translationIP):
		self.add_param('translationIP', translationIP)

	def get_aclRules(self):
		return self.get_params().get('aclRules')

	def set_aclRules(self, aclRules):
		self.add_param('aclRules', aclRules)

