#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifySecurityGroupPolicyRequest(Request):

	def __init__(self):
		Request.__init__(self, 'dfw', 'qcloudcliV1', 'ModifySecurityGroupPolicy', 'dfw.api.qcloud.com')

	def get_sgId(self):
		return self.get_params().get('sgId')

	def set_sgId(self, sgId):
		self.add_param('sgId', sgId)

	def get_ingress(self):
		return self.get_params().get('ingress')

	def set_ingress(self, ingress):
		self.add_param('ingress', ingress)

	def get_egress(self):
		return self.get_params().get('egress')

	def set_egress(self, egress):
		self.add_param('egress', egress)

