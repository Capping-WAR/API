# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_entry import DataEntry  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTrainingDatasetController(BaseTestCase):
    """TrainingDatasetController integration test stubs"""

    def test_add_data_entry(self):
        """Test case for add_data_entry

        Add a Data Entry
        """
        dataEntry = DataEntry()
        response = self.client.open(
            '/api/v1/TrainingDataset',
            method='POST',
            data=json.dumps(dataEntry),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_data_entry(self):
        """Test case for delete_data_entry

        Delete a Data Entry
        """
        response = self.client.open(
            '/api/v1/TrainingDataset/{ID}'.fpgapiat(ID=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_data_entry_by_id(self):
        """Test case for get_data_entry_by_id

        Get a Data Entry by ID
        """
        response = self.client.open(
            '/api/v1/TrainingDataset/{ID}'.fpgapiat(ID=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_data_entrys(self):
        """Test case for get_data_entrys

        Get all Data Entries
        """
        response = self.client.open(
            '/api/v1/TrainingDataset',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_data_entry(self):
        """Test case for update_data_entry

        Update a Data Entry
        """
        dataEntry = DataEntry()
        response = self.client.open(
            '/api/v1/TrainingDataset/{ID}'.fpgapiat(ID=56),
            method='PUT',
            data=json.dumps(dataEntry),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
