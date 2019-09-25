# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.version import Version  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVersionController(BaseTestCase):
    """VersionController integration test stubs"""

    def test_add_version(self):
        """Test case for add_version

        Add a Version
        """
        Version = Version()
        response = self.client.open(
            '/api/v1/version',
            method='POST',
            data=json.dumps(Version),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_version(self):
        """Test case for delete_version

        Delete a Version
        """
        response = self.client.open(
            '/api/v1/version/{modelID}'.format(modelID=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_version_by_id(self):
        """Test case for get_version_by_id

        Get a model version by modelID
        """
        response = self.client.open(
            '/api/v1/version/{modelID}'.format(modelID=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_versions(self):
        """Test case for get_versions

        Get all Versions
        """
        response = self.client.open(
            '/api/v1/versions',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_version(self):
        """Test case for update_version

        Update a Version
        """
        Version = Version()
        response = self.client.open(
            '/api/v1/version/{modelID}'.format(modelID=56),
            method='PUT',
            data=json.dumps(Version),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
