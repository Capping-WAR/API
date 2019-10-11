# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.sentence_rule import SentenceRule  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSentenceRulesController(BaseTestCase):
    """SentenceRulesController integration test stubs"""

    def test_add_sentence_rule(self):
        """Test case for add_sentence_rule

        Add a Sentence Rule
        """
        sentence_rule = SentenceRule()
        response = self.client.open(
            '/api/v1/sentenceRule',
            method='POST',
            data=json.dumps(sentence_rule),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_sentence_rule(self):
        """Test case for delete_sentence_rule

        Delete a Sentence Rule
        """
        response = self.client.open(
            '/api/v1/sentenceRule/{sentenceID}'.format(sentenceID=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_sentence_rule_by_id(self):
        """Test case for get_sentence_rule_by_id

        Get a Sentence Rule by sentenceID
        """
        response = self.client.open(
            '/api/v1/sentenceRule/{sentenceID}'.format(sentenceID=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_sentence_rules(self):
        """Test case for get_sentence_rules

        Get all Sentence Rules
        """
        response = self.client.open(
            '/api/v1/sentenceRules',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_sentence_rule(self):
        """Test case for update_sentence_rule

        Update a Sentence Rule
        """
        sentence_rule = SentenceRule()
        response = self.client.open(
            '/api/v1/sentenceRule/{sentenceID}'.format(sentenceID=56),
            method='PUT',
            data=json.dumps(sentence_rule),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
