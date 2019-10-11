# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.query import Query  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUtilsController(BaseTestCase):
    """UtilsController integration test stubs"""

    def test_get_search_results(self):
        """Test case for get_search_results

        Runs a given SELECT Query
        """
        query = Query()
        response = self.client.open(
            '/api/v1/search',
            method='GET',
            data=json.dumps(query),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
