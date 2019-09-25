# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Version(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, model_id: int=None, bal_accuracy: float=None, rule_num: int=None, location: str=None, date_added: str=None):  # noqa: E501
        """Version - a model defined in Swagger

        :param model_id: The model_id of this Version.  # noqa: E501
        :type model_id: int
        :param bal_accuracy: The bal_accuracy of this Version.  # noqa: E501
        :type bal_accuracy: float
        :param rule_num: The rule_num of this Version.  # noqa: E501
        :type rule_num: int
        :param location: The location of this Version.  # noqa: E501
        :type location: str
        :param date_added: The date_added of this Version.  # noqa: E501
        :type date_added: str
        """
        self.swagger_types = {
            'model_id': int,
            'bal_accuracy': float,
            'rule_num': int,
            'location': str,
            'date_added': str
        }

        self.attribute_map = {
            'model_id': 'modelID',
            'bal_accuracy': 'balAccuracy',
            'rule_num': 'ruleNum',
            'location': 'location',
            'date_added': 'dateAdded'
        }

        self._model_id = model_id
        self._bal_accuracy = bal_accuracy
        self._rule_num = rule_num
        self._location = location
        self._date_added = date_added

    @classmethod
    def from_dict(cls, dikt) -> 'Version':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The version of this Version.  # noqa: E501
        :rtype: Version
        """
        return util.deserialize_model(dikt, cls)

    @property
    def model_id(self) -> int:
        """Gets the model_id of this Version.

        Unique ID of the model  # noqa: E501

        :return: The model_id of this Version.
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id: int):
        """Sets the model_id of this Version.

        Unique ID of the model  # noqa: E501

        :param model_id: The model_id of this Version.
        :type model_id: int
        """

        self._model_id = model_id

    @property
    def bal_accuracy(self) -> float:
        """Gets the bal_accuracy of this Version.

        Percentage Accuracy of the model  # noqa: E501

        :return: The bal_accuracy of this Version.
        :rtype: float
        """
        return self._bal_accuracy

    @bal_accuracy.setter
    def bal_accuracy(self, bal_accuracy: float):
        """Sets the bal_accuracy of this Version.

        Percentage Accuracy of the model  # noqa: E501

        :param bal_accuracy: The bal_accuracy of this Version.
        :type bal_accuracy: float
        """
        if bal_accuracy is None:
            raise ValueError("Invalid value for `bal_accuracy`, must not be `None`")  # noqa: E501

        self._bal_accuracy = bal_accuracy

    @property
    def rule_num(self) -> int:
        """Gets the rule_num of this Version.

        Rule model coincides with  # noqa: E501

        :return: The rule_num of this Version.
        :rtype: int
        """
        return self._rule_num

    @rule_num.setter
    def rule_num(self, rule_num: int):
        """Sets the rule_num of this Version.

        Rule model coincides with  # noqa: E501

        :param rule_num: The rule_num of this Version.
        :type rule_num: int
        """
        if rule_num is None:
            raise ValueError("Invalid value for `rule_num`, must not be `None`")  # noqa: E501

        self._rule_num = rule_num

    @property
    def location(self) -> str:
        """Gets the location of this Version.

        absolute path to model on disk  # noqa: E501

        :return: The location of this Version.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this Version.

        absolute path to model on disk  # noqa: E501

        :param location: The location of this Version.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def date_added(self) -> str:
        """Gets the date_added of this Version.

        Date added to the database  # noqa: E501

        :return: The date_added of this Version.
        :rtype: str
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added: str):
        """Sets the date_added of this Version.

        Date added to the database  # noqa: E501

        :param date_added: The date_added of this Version.
        :type date_added: str
        """
        if date_added is None:
            raise ValueError("Invalid value for `date_added`, must not be `None`")  # noqa: E501

        self._date_added = date_added
