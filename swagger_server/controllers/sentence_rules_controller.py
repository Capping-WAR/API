import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.sentence_rule import SentenceRule  # noqa: E501
from swagger_server import util


def add_sentence_rule(sentence_rule):  # noqa: E501
    """Add a Sentence Rule

     # noqa: E501

    :param sentence_rule: Sentence Rule to be added
    :type sentence_rule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        sentence_rule = SentenceRule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_sentence_rule(sentenceID):  # noqa: E501
    """Delete a Sentence Rule

     # noqa: E501

    :param sentenceID: sentence ID of Sentence Rule
    :type sentenceID: int

    :rtype: None
    """
    return 'do some magic!'


def get_sentence_rule_by_id(sentenceID):  # noqa: E501
    """Get a Sentence Rule by sentenceID

     # noqa: E501

    :param sentenceID: sentence ID of Sentence Rule
    :type sentenceID: int

    :rtype: List[SentenceRule]
    """
    return 'do some magic!'


def get_sentence_rules():  # noqa: E501
    """Get all Sentence Rules

     # noqa: E501


    :rtype: List[SentenceRule]
    """
    return 'do some magic!'


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
        sentence_rule = SentenceRule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
