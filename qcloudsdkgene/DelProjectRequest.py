#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DelProjectRequest(Request):

	def __init__(self):
		Request.__init__(self, 'gene', 'qcloudcliV1', 'DelProject', 'gene.api.qcloud.com')

