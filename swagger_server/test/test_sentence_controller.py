# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.sentence import Sentence  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSentenceController(BaseTestCase):
    """SentenceController integration test stubs"""

    def test_add_sentence(self):
        """Test case for add_sentence

        Add a Sentence
        """
        survey = Sentence()
        response = self.client.open(
            '/api/v1/sentence',
            method='POST',
            data=json.dumps(survey),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_sentence(self):
        """Test case for delete_sentence

        Delete a Sentence
        """
        response = self.client.open(
            '/api/v1/sentence/{sentenceID}'.format(sentenceID='sentenceID_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_sentence_by_id(self):
        """Test case for get_sentence_by_id

        Get a Sentence by ID
        """
        response = self.client.open(
            '/api/v1/sentence/{sentenceID}'.format(sentenceID='sentenceID_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_sentences(self):
        """Test case for get_sentences

        Get all Sentences
        """
        response = self.client.open(
            '/api/v1/sentences',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_sentence(self):
        """Test case for update_sentence

        Update a Sentence
        """
        survey = Sentence()
        response = self.client.open(
            '/api/v1/sentence/{sentenceID}'.format(sentenceID='sentenceID_example'),
            method='PUT',
            data=json.dumps(survey),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
