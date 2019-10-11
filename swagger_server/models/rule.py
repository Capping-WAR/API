# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Rule(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, rule_id: int=None, rule_name: str=None, description: str=None, priority: int=None):  # noqa: E501
        """Rule - a model defined in Swagger

        :param rule_id: The rule_id of this Rule.  # noqa: E501
        :type rule_id: int
        :param rule_name: The rule_name of this Rule.  # noqa: E501
        :type rule_name: str
        :param description: The description of this Rule.  # noqa: E501
        :type description: str
        :param priority: The priority of this Rule.  # noqa: E501
        :type priority: int
        """
        self.swagger_types = {
            'rule_id': int,
            'rule_name': str,
            'description': str,
            'priority': int
        }

        self.attribute_map = {
            'rule_id': 'ruleID',
            'rule_name': 'ruleName',
            'description': 'description',
            'priority': 'priority'
        }

        self._rule_id = rule_id
        self._rule_name = rule_name
        self._description = description
        self._priority = priority

    @classmethod
    def from_dict(cls, dikt) -> 'Rule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The rule of this Rule.  # noqa: E501
        :rtype: Rule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rule_id(self) -> int:
        """Gets the rule_id of this Rule.

        Unique ID of the rule  # noqa: E501

        :return: The rule_id of this Rule.
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id: int):
        """Sets the rule_id of this Rule.

        Unique ID of the rule  # noqa: E501

        :param rule_id: The rule_id of this Rule.
        :type rule_id: int
        """

        self._rule_id = rule_id

    @property
    def rule_name(self) -> str:
        """Gets the rule_name of this Rule.

        name of rule  # noqa: E501

        :return: The rule_name of this Rule.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name: str):
        """Sets the rule_name of this Rule.

        name of rule  # noqa: E501

        :param rule_name: The rule_name of this Rule.
        :type rule_name: str
        """
        if rule_name is None:
            raise ValueError("Invalid value for `rule_name`, must not be `None`")  # noqa: E501

        self._rule_name = rule_name

    @property
    def description(self) -> str:
        """Gets the description of this Rule.

        description of rule  # noqa: E501

        :return: The description of this Rule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Rule.

        description of rule  # noqa: E501

        :param description: The description of this Rule.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def priority(self) -> int:
        """Gets the priority of this Rule.

        the current value it has towards the dataset, used to get more of a ceartin rule  # noqa: E501

        :return: The priority of this Rule.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority: int):
        """Sets the priority of this Rule.

        the current value it has towards the dataset, used to get more of a ceartin rule  # noqa: E501

        :param priority: The priority of this Rule.
        :type priority: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority
