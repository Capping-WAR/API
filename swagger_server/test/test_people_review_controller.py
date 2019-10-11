# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.people_review import PeopleReview  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPeopleReviewController(BaseTestCase):
    """PeopleReviewController integration test stubs"""

    def test_add_people_review(self):
        """Test case for add_people_review

        Add a People Review
        """
        people_review = PeopleReview()
        response = self.client.open(
            '/api/v1/review',
            method='POST',
            data=json.dumps(people_review),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_people_review(self):
        """Test case for delete_people_review

        Delete a People Review
        """
        response = self.client.open(
            '/api/v1/review/{peopleReviewID}'.format(peopleReviewID=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_people_review_by_id(self):
        """Test case for get_people_review_by_id

        Get a People Review by ID
        """
        response = self.client.open(
            '/api/v1/review/{peopleReviewID}'.format(peopleReviewID=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_people_reviews(self):
        """Test case for get_people_reviews

        Get all People Reviews
        """
        response = self.client.open(
            '/api/v1/reviews',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_people_review(self):
        """Test case for update_people_review

        Update a People Review
        """
        people_review = PeopleReview()
        response = self.client.open(
            '/api/v1/review/{peopleReviewID}'.format(peopleReviewID=56),
            method='PUT',
            data=json.dumps(people_review),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
