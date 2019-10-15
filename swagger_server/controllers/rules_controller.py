import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.rule import Rule  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals

def add_rule(Rule):  # noqa: E501
    """Add a Rule

     # noqa: E501

    :param Rule: Rule to be added
    :type Rule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        values = list(Rule.values())
        cols = ','.join(list(Rule.keys()))
        results =  _globals.orm.insert('Rules', values, cols=cols)
        if type(results) != list:
            results = str(results)
            
        return results

def delete_rule(ruleID):  # noqa: E501
    """Delete a Rule

     # noqa: E501

    :param ruleID: ID of Rule
    :type ruleID: int

    :rtype: None
    """
    results = _globals.orm.delete(
        'Rules', 
        clause=f'WHERE ruleID={ruleID}'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def get_rule_by_id(ruleID):  # noqa: E501
    """Get a Rule by ruleID

     # noqa: E501

    :param ruleID: ID of Rule
    :type ruleID: int

    :rtype: List[Rule]
    """
    results = _globals.orm.get(
        'Rules', 
        clause=f'WHERE ruleID={ruleID}'
    ) 
    if type(results) != list:
        results = str(results)
    return {'Rule':results}


def get_rules():  # noqa: E501
    """Get all Rules

     # noqa: E501


    :rtype: List[Rule]
    """
    results = _globals.orm.get(
        'Rules', 
    ) 
    if type(results) != list:
        results = str(results)
    return {'Rules':results}


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
        results = _globals.orm.update(
            'Rules',
            Rule,
            clause=f'WHERE ruleID={ruleID}'
        ) 
        if type(results) != list:
            results = str(results)
        return results