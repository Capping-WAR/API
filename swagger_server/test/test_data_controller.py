# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.datapoint import Datapoint  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDataController(BaseTestCase):
    """DataController integration test stubs"""

    def test_add_datapoint(self):
        """Test case for add_datapoint

        Add a Datapoint
        """
        Datapoint = Datapoint()
        response = self.client.open(
            '/v1/Data',
            method='POST',
            data=json.dumps(Datapoint),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_datapoint(self):
        """Test case for delete_datapoint

        Delete a Datapoint
        """
        response = self.client.open(
            '/v1/data/{sentenceID}'.format(sentenceID='sentenceID_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_datapoint_by_id(self):
        """Test case for get_datapoint_by_id

        Get a datapoint by sentence ID
        """
        response = self.client.open(
            '/v1/data/{sentenceID}'.format(sentenceID='sentenceID_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_datapoints(self):
        """Test case for get_datapoints

        Get all Datapoints
        """
        response = self.client.open(
            '/v1/Data',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_datapoint(self):
        """Test case for update_datapoint

        Update a Datapoint
        """
        Datapoint = Datapoint()
        response = self.client.open(
            '/v1/data/{sentenceID}'.format(sentenceID='sentenceID_example'),
            method='PUT',
            data=json.dumps(Datapoint),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
