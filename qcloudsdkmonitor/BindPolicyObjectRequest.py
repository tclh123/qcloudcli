#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class BindPolicyObjectRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'BindPolicyObject', 'monitor.api.qcloud.com')

	def get_groupId(self):
		return self.get_params().get('groupId')

	def set_groupId(self, groupId):
		self.add_param('groupId', groupId)

	def get_dimensions(self):
		return self.get_params().get('dimensions')

	def set_dimensions(self, dimensions):
		self.add_param('dimensions', dimensions)

