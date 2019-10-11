import connexion
import six

from swagger_server.models.model import Model  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server import util


def add_model(Model):  # noqa: E501
    """Add a Model

     # noqa: E501

    :param Model: Model to be added
    :type Model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Model = Model.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_model(modelID):  # noqa: E501
    """Delete a Model

     # noqa: E501

    :param modelID: ID of Model
    :type modelID: int

    :rtype: None
    """
    return 'do some magic!'


def get_model_by_id(modelID):  # noqa: E501
    """Get a model version by modelID

     # noqa: E501

    :param modelID: ID of Model
    :type modelID: int

    :rtype: List[Model]
    """
    return 'do some magic!'


def get_models():  # noqa: E501
    """Get all Models

     # noqa: E501


    :rtype: List[Model]
    """
    return 'do some magic!'


def update_model(modelID, Model):  # noqa: E501
    """Update a Model

     # noqa: E501

    :param modelID: ID of Model
    :type modelID: int
    :param Model: Updated Model
    :type Model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Model = Model.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
