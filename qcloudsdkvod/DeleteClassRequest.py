#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteClassRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vod', 'qcloudcliV1', 'DeleteClass', 'vod.api.qcloud.com')

	def get_classId(self):
		return self.get_params().get('classId')

	def set_classId(self, classId):
		self.add_param('classId', classId)

