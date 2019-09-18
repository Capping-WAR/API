import connexion
import six

from swagger_server.models.datapoint import Datapoint  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server import util


def add_datapoint(Datapoint):  # noqa: E501
    """Add a Datapoint

     # noqa: E501

    :param Datapoint: Datapoint to be added
    :type Datapoint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Datapoint = Datapoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_datapoint(sentenceID):  # noqa: E501
    """Delete a Datapoint

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: str

    :rtype: None
    """
    return 'do some magic!'


def get_datapoint_by_id(sentenceID):  # noqa: E501
    """Get a datapoint by sentence ID

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: str

    :rtype: List[Datapoint]
    """
    return 'do some magic!'


def get_datapoints():  # noqa: E501
    """Get all Datapoints

     # noqa: E501


    :rtype: List[Datapoint]
    """
    return 'do some magic!'


def update_datapoint(sentenceID, Datapoint):  # noqa: E501
    """Update a Datapoint

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: str
    :param Datapoint: New Version of the Datapoint
    :type Datapoint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Datapoint = Datapoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
