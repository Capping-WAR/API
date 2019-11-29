# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Reviewer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, reviewer_id: int=None, email_address: str=None, first_name: str=None, last_name: str=None, is_admin: bool=None, reputation: int=None):  # noqa: E501
        """Reviewer - a model defined in Swagger

        :param reviewer_id: The reviewer_id of this Reviewer.  # noqa: E501
        :type reviewer_id: int
        :param email_address: The email_address of this Reviewer.  # noqa: E501
        :type email_address: str
        :param first_name: The first_name of this Reviewer.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Reviewer.  # noqa: E501
        :type last_name: str
        :param is_admin: The is_admin of this Reviewer.  # noqa: E501
        :type is_admin: bool
        :param reputation: The reputation of this Reviewer.  # noqa: E501
        :type reputation: int
        """
        self.swagger_types = {
            'reviewer_id': int,
            'email_address': str,
            'first_name': str,
            'last_name': str,
            'is_admin': bool,
            'reputation': int
        }

        self.attribute_map = {
            'reviewer_id': 'reviewerID',
            'email_address': 'emailAddress',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'is_admin': 'isAdmin',
            'reputation': 'reputation'
        }

        self._reviewer_id = reviewer_id
        self._email_address = email_address
        self._first_name = first_name
        self._last_name = last_name
        self._is_admin = is_admin
        self._reputation = reputation

    @classmethod
    def from_dict(cls, dikt) -> 'Reviewer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The reviewer of this Reviewer.  # noqa: E501
        :rtype: Reviewer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reviewer_id(self) -> int:
        """Gets the reviewer_id of this Reviewer.

        Unique ID of the reviewer  # noqa: E501

        :return: The reviewer_id of this Reviewer.
        :rtype: int
        """
        return self._reviewer_id

    @reviewer_id.setter
    def reviewer_id(self, reviewer_id: int):
        """Sets the reviewer_id of this Reviewer.

        Unique ID of the reviewer  # noqa: E501

        :param reviewer_id: The reviewer_id of this Reviewer.
        :type reviewer_id: int
        """

        self._reviewer_id = reviewer_id

    @property
    def email_address(self) -> str:
        """Gets the email_address of this Reviewer.

        :\"Email address of the reviewer\"  # noqa: E501

        :return: The email_address of this Reviewer.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address: str):
        """Sets the email_address of this Reviewer.

        :\"Email address of the reviewer\"  # noqa: E501

        :param email_address: The email_address of this Reviewer.
        :type email_address: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Reviewer.

        The first name of the user  # noqa: E501

        :return: The first_name of this Reviewer.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Reviewer.

        The first name of the user  # noqa: E501

        :param first_name: The first_name of this Reviewer.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this Reviewer.

        The last name of the user  # noqa: E501

        :return: The last_name of this Reviewer.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this Reviewer.

        The last name of the user  # noqa: E501

        :param last_name: The last_name of this Reviewer.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def is_admin(self) -> bool:
        """Gets the is_admin of this Reviewer.

        Denotes wether this user has admin privileges  # noqa: E501

        :return: The is_admin of this Reviewer.
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin: bool):
        """Sets the is_admin of this Reviewer.

        Denotes wether this user has admin privileges  # noqa: E501

        :param is_admin: The is_admin of this Reviewer.
        :type is_admin: bool
        """
        if is_admin is None:
            raise ValueError("Invalid value for `is_admin`, must not be `None`")  # noqa: E501

        self._is_admin = is_admin

    @property
    def reputation(self) -> int:
        """Gets the reputation of this Reviewer.

        The user's ranking as a reviewer  # noqa: E501

        :return: The reputation of this Reviewer.
        :rtype: int
        """
        return self._reputation

    @reputation.setter
    def reputation(self, reputation: int):
        """Sets the reputation of this Reviewer.

        The user's ranking as a reviewer  # noqa: E501

        :param reputation: The reputation of this Reviewer.
        :type reputation: int
        """
        if reputation is None:
            raise ValueError("Invalid value for `reputation`, must not be `None`")  # noqa: E501

        self._reputation = reputation
