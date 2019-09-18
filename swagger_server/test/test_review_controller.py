# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.review import Review  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReviewController(BaseTestCase):
    """ReviewController integration test stubs"""

    def test_add_review(self):
        """Test case for add_review

        Add a Review
        """
        survey = Review()
        response = self.client.open(
            '/v1/review',
            method='POST',
            data=json.dumps(survey),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_review(self):
        """Test case for delete_review

        Delete a Review
        """
        response = self.client.open(
            '/v1/review/{reviewID}'.format(reviewID='reviewID_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_review_by_id(self):
        """Test case for get_review_by_id

        Get a Review by ID
        """
        response = self.client.open(
            '/v1/review/{reviewID}'.format(reviewID='reviewID_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reviews(self):
        """Test case for get_reviews

        Get all Reviews
        """
        response = self.client.open(
            '/v1/reviews',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_review(self):
        """Test case for update_review

        Update a Review
        """
        survey = Review()
        response = self.client.open(
            '/v1/review/{reviewID}'.format(reviewID='reviewID_example'),
            method='PUT',
            data=json.dumps(survey),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
