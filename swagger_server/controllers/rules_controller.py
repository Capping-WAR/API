import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.rule import Rule  # noqa: E501
from swagger_server import util


def add_rule(Rule):  # noqa: E501
    """Add a Rule

     # noqa: E501

    :param Rule: Rule to be added
    :type Rule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Rule = Rule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_rule(ruleID):  # noqa: E501
    """Delete a Rule

     # noqa: E501

    :param ruleID: ID of Rule
    :type ruleID: int

    :rtype: None
    """
    return 'do some magic!'


def get_rule_by_id(ruleID):  # noqa: E501
    """Get a Rule by ruleID

     # noqa: E501

    :param ruleID: ID of Rule
    :type ruleID: int

    :rtype: List[Rule]
    """
    return 'do some magic!'


def get_rules():  # noqa: E501
    """Get all Rules

     # noqa: E501


    :rtype: List[Rule]
    """
    return 'do some magic!'


def update_rule(ruleID, Rule):  # noqa: E501
    """Update a Rule

     # noqa: E501

    :param ruleID: ID of Rule
    :type ruleID: int
    :param Rule: Updated Rule
    :type Rule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Rule = Rule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
