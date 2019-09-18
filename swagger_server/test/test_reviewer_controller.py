# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.reviewer import Reviewer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReviewerController(BaseTestCase):
    """ReviewerController integration test stubs"""

    def test_add_reviewer(self):
        """Test case for add_reviewer

        Add a Reviewer
        """
        survey = Reviewer()
        response = self.client.open(
            '/api/v1/reviewer',
            method='POST',
            data=json.dumps(survey),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_reviewer(self):
        """Test case for delete_reviewer

        Delete a Reviewer
        """
        response = self.client.open(
            '/api/v1/reviewer/{reviewerID}'.format(reviewerID='reviewerID_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reviewer_by_id(self):
        """Test case for get_reviewer_by_id

        Get a Reviewer by ID
        """
        response = self.client.open(
            '/api/v1/reviewer/{reviewerID}'.format(reviewerID='reviewerID_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reviewers(self):
        """Test case for get_reviewers

        Get all Reviewers
        """
        response = self.client.open(
            '/api/v1/reviewers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_reviewer(self):
        """Test case for update_reviewer

        Update a Reviewer
        """
        survey = Reviewer()
        response = self.client.open(
            '/api/v1/reviewer/{reviewerID}'.format(reviewerID='reviewerID_example'),
            method='PUT',
            data=json.dumps(survey),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
