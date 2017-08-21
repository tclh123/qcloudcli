#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetImageShareUinInfoRequest(Request):

	def __init__(self):
		Request.__init__(self, 'image', 'qcloudcliV1', 'GetImageShareUinInfo', 'image.api.qcloud.com')

	def get_imageIds(self):
		return self.get_params().get('imageIds')

	def set_imageIds(self, imageIds):
		self.add_param('imageIds', imageIds)

