# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSiteStatisticsController(BaseTestCase):
    """SiteStatisticsController integration test stubs"""

    def test_post_login_stats(self):
        """Test case for post_login_stats

        updates current login statistics count
        """
        response = self.client.open(
            '/api/v1/loginStats',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_user_stats(self):
        """Test case for post_user_stats

        updates current user statistics count
        """
        user_info = UserInfo()
        response = self.client.open(
            '/api/v1/userStats',
            method='POST',
            data=json.dumps(user_info),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
