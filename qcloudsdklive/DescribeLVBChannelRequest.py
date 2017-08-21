#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeLVBChannelRequest(Request):

	def __init__(self):
		Request.__init__(self, 'live', 'qcloudcliV1', 'DescribeLVBChannel', 'live.api.qcloud.com')

	def get_channelId(self):
		return self.get_params().get('channelId')

	def set_channelId(self, channelId):
		self.add_param('channelId', channelId)

