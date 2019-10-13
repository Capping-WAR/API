import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.sentence import Sentence  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals

def add_sentence(sentence):  # noqa: E501
    """Add a Sentence

     # noqa: E501

    :param sentence: Sentence to be added
    :type sentence: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        values = list(sentence.values())
        cols = ','.join(list(sentence.keys()))
        results =  _globals.orm.insert('sentences', values, cols=cols)
        if type(results) != list:
            results = str(results)
            
        return results



def delete_sentence(sentenceID):  # noqa: E501
    """Delete a Sentence

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: int

    :rtype: None
    """
    return 'do some magic!'


def get_sentence_by_id(sentenceID):  # noqa: E501
    """Get a Sentence by ID

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: int

    :rtype: List[Sentence]
    """
    return 'do some magic!'


def get_sentences():  # noqa: E501
    """Get all Sentences

     # noqa: E501


    :rtype: List[Sentence]
    """
    return 'do some magic!'


def update_sentence(sentenceID, sentence):  # noqa: E501
    """Update a Sentence

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: int
    :param sentence: New Version of the Sentence
    :type sentence: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        sentence = Sentence.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
