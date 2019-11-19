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
            method='POST',
            data=json.dumps(query),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_retrain(self):
        """Test case for post_retrain

        checks for new entries in the traning data set table and sends a request to train a new model if one is found
        """
        response = self.client.open(
            '/api/v1/retrain',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
