# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.model_review import ModelReview  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.rule import Rule  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModelReviewsController(BaseTestCase):
    """ModelReviewsController integration test stubs"""

    def test_add_model_review(self):
        """Test case for add_model_review

        Add a Model Review
        """
        model_review = ModelReview()
        response = self.client.open(
            '/api/v1/modelReview',
            method='POST',
            data=json.dumps(model_review),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_model_review(self):
        """Test case for delete_model_review

        Delete a Model Review
        """
        response = self.client.open(
            '/api/v1/modelReview/{sentenceID}'.fpgapiat(sentenceID=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_model_review_by_id(self):
        """Test case for get_model_review_by_id

        Get a Rule by sentenceID
        """
        response = self.client.open(
            '/api/v1/modelReview/{sentenceID}'.fpgapiat(sentenceID=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_model_reviews(self):
        """Test case for get_model_reviews

        Get all Model Reviews
        """
        response = self.client.open(
            '/api/v1/modelReviews',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_model_review(self):
        """Test case for update_model_review

        Update a Model Review
        """
        Model_Review = Rule()
        response = self.client.open(
            '/api/v1/modelReview/{sentenceID}'.fpgapiat(sentenceID=56),
            method='PUT',
            data=json.dumps(Model_Review),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
