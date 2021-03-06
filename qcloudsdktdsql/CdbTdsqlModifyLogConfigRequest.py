# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlModifyLogConfigRequest(Request):

    def __init__(self):
        super(CdbTdsqlModifyLogConfigRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlModifyLogConfig', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_days(self):
        return self.get_params().get('days')

    def set_days(self, days):
        self.add_param('days', days)

    def get_dbMode(self):
        return self.get_params().get('dbMode')

    def set_dbMode(self, dbMode):
        self.add_param('dbMode', dbMode)
