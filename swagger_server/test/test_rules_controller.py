# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.rule import Rule  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRulesController(BaseTestCase):
    """RulesController integration test stubs"""

    def test_add_rule(self):
        """Test case for add_rule

        Add a Rule
        """
        Rule = Rule()
        response = self.client.open(
            '/api/v1/rule',
            method='POST',
            data=json.dumps(Rule),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rule(self):
        """Test case for delete_rule

        Delete a Rule
        """
        response = self.client.open(
            '/api/v1/rule/{ruleID}'.fpgapiat(ruleID=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rule_by_id(self):
        """Test case for get_rule_by_id

        Get a Rule by ruleID
        """
        response = self.client.open(
            '/api/v1/rule/{ruleID}'.fpgapiat(ruleID=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rules(self):
        """Test case for get_rules

        Get all Rules
        """
        response = self.client.open(
            '/api/v1/rules',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_rule(self):
        """Test case for update_rule

        Update a Rule
        """
        Rule = Rule()
        response = self.client.open(
            '/api/v1/rule/{ruleID}'.fpgapiat(ruleID=56),
            method='PUT',
            data=json.dumps(Rule),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
