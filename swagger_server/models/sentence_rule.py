# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SentenceRule(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sentence_id: int=None, tagged_rule_id: int=None, status: str=None):  # noqa: E501
        """SentenceRule - a model defined in Swagger

        :param sentence_id: The sentence_id of this SentenceRule.  # noqa: E501
        :type sentence_id: int
        :param tagged_rule_id: The tagged_rule_id of this SentenceRule.  # noqa: E501
        :type tagged_rule_id: int
        :param status: The status of this SentenceRule.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'sentence_id': int,
            'tagged_rule_id': int,
            'status': str
        }

        self.attribute_map = {
            'sentence_id': 'sentenceID',
            'tagged_rule_id': 'taggedRuleID',
            'status': 'status'
        }

        self._sentence_id = sentence_id
        self._tagged_rule_id = tagged_rule_id
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'SentenceRule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The sentence_rule of this SentenceRule.  # noqa: E501
        :rtype: SentenceRule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sentence_id(self) -> int:
        """Gets the sentence_id of this SentenceRule.

        Unique ID of the sentence that was submitted for review  # noqa: E501

        :return: The sentence_id of this SentenceRule.
        :rtype: int
        """
        return self._sentence_id

    @sentence_id.setter
    def sentence_id(self, sentence_id: int):
        """Sets the sentence_id of this SentenceRule.

        Unique ID of the sentence that was submitted for review  # noqa: E501

        :param sentence_id: The sentence_id of this SentenceRule.
        :type sentence_id: int
        """

        self._sentence_id = sentence_id

    @property
    def tagged_rule_id(self) -> int:
        """Gets the tagged_rule_id of this SentenceRule.

        the rule tagged for review by the user  # noqa: E501

        :return: The tagged_rule_id of this SentenceRule.
        :rtype: int
        """
        return self._tagged_rule_id

    @tagged_rule_id.setter
    def tagged_rule_id(self, tagged_rule_id: int):
        """Sets the tagged_rule_id of this SentenceRule.

        the rule tagged for review by the user  # noqa: E501

        :param tagged_rule_id: The tagged_rule_id of this SentenceRule.
        :type tagged_rule_id: int
        """

        self._tagged_rule_id = tagged_rule_id

    @property
    def status(self) -> str:
        """Gets the status of this SentenceRule.

        the current status of the sentence in its review process  # noqa: E501

        :return: The status of this SentenceRule.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this SentenceRule.

        the current status of the sentence in its review process  # noqa: E501

        :param status: The status of this SentenceRule.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status
