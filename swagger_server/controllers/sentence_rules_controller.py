import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.sentence_rule import SentenceRule  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals


def add_sentence_rule(sentence_rule):  # noqa: E501
    """Add a Sentence Rule

     # noqa: E501

    :param sentence_rule: Sentence Rule to be added
    :type sentence_rule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        values = list(sentence_rule.values())
        cols = ','.join(list(sentence_rule.keys()))
        results =  _globals.orm.insert('SentenceRules', values, cols=cols)
        if type(results) != list:
            results = str(results)
            
        return results


def delete_sentence_rule(sentenceID):  # noqa: E501
    """Delete a Sentence Rule

     # noqa: E501

    :param sentenceID: sentence ID of Sentence Rule
    :type sentenceID: int

    :rtype: None
    """
    results = _globals.orm.delete(
        'SentenceRules', 
        clause=f'WHERE sentenceID={sentenceID}'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def get_sentence_rule_by_id(sentenceID):  # noqa: E501
    """Get a Sentence Rule by sentenceID

     # noqa: E501

    :param sentenceID: sentence ID of Sentence Rule
    :type sentenceID: int

    :rtype: List[SentenceRule]
    """
    results = _globals.orm.get(
        'SentenceRules', 
        clause=f'WHERE sentenceID={sentenceID}'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def get_sentence_rules():  # noqa: E501
    """Get all Sentence Rules

     # noqa: E501


    :rtype: List[SentenceRule]
    """
    results = _globals.orm.get(
        'SentenceRules'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def update_sentence_rule(sentenceID, sentence_rule):  # noqa: E501
    """Update a Sentence Rule

     # noqa: E501

    :param sentenceID: sentence ID of Sentence Rule
    :type sentenceID: int
    :param sentence_rule: Updated Sentence Rule
    :type sentence_rule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        results = _globals.orm.update(
            'SentenceRules',
            sentence_rule,
            clause=f'WHERE sentenceID={sentenceID}'
        ) 
        if type(results) != list:
            results = str(results)
        return results