# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.model import Model  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModelsController(BaseTestCase):
    """ModelsController integration test stubs"""

    def test_add_model(self):
        """Test case for add_model

        Add a Model
        """
        Model = Model()
        response = self.client.open(
            '/api/v1/model',
            method='POST',
            data=json.dumps(Model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_model(self):
        """Test case for delete_model

        Delete a Model
        """
        response = self.client.open(
            '/api/v1/model/{modelID}'.format(modelID=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_model_by_id(self):
        """Test case for get_model_by_id

        Get a model version by modelID
        """
        response = self.client.open(
            '/api/v1/model/{modelID}'.format(modelID=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_models(self):
        """Test case for get_models

        Get all Models
        """
        response = self.client.open(
            '/api/v1/models',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_model(self):
        """Test case for update_model

        Update a Model
        """
        Model = Model()
        response = self.client.open(
            '/api/v1/model/{modelID}'.format(modelID=56),
            method='PUT',
            data=json.dumps(Model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
