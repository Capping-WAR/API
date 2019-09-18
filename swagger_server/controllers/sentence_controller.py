import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.sentence import Sentence  # noqa: E501
from swagger_server import util


def add_sentence(survey):  # noqa: E501
    """Add a Sentence

     # noqa: E501

    :param survey: Sentence to be added
    :type survey: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        survey = Sentence.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_sentence(sentenceID):  # noqa: E501
    """Delete a Sentence

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: str

    :rtype: None
    """
    return 'do some magic!'


def get_sentence_by_id(sentenceID):  # noqa: E501
    """Get a Sentence by ID

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: str

    :rtype: List[Sentence]
    """
    return 'do some magic!'


def get_sentences():  # noqa: E501
    """Get all Sentences

     # noqa: E501


    :rtype: List[Sentence]
    """
    return 'do some magic!'


def update_sentence(sentenceID, survey):  # noqa: E501
    """Update a Sentence

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: str
    :param survey: New Version of the Sentence
    :type survey: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        survey = Sentence.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
