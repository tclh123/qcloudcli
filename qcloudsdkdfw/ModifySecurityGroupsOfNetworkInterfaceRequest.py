#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifySecurityGroupsOfNetworkInterfaceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'dfw', 'qcloudcliV1', 'ModifySecurityGroupsOfNetworkInterface', 'dfw.api.qcloud.com')

	def get_networkInterfaceSet(self):
		return self.get_params().get('networkInterfaceSet')

	def set_networkInterfaceSet(self, networkInterfaceSet):
		self.add_param('networkInterfaceSet', networkInterfaceSet)

