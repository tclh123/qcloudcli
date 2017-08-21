#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DetachUserPolicyRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cam', 'qcloudcliV1', 'DetachUserPolicy', 'cam.api.qcloud.com')

	def get_uin(self):
		return self.get_params().get('uin')

	def set_uin(self, uin):
		self.add_param('uin', uin)

