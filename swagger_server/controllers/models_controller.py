import connexion
import six

from swagger_server.models.model import Model  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals


def add_model(Model):  # noqa: E501
    """Add a Model

     # noqa: E501

    :param Model: Model to be added
    :type Model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        values = list(Model.values())
        cols = ','.join(list(Model.keys()))
        results =  _globals.orm.insert('Models', values, cols=cols)
        if type(results) != list:
            results = str(results)
            
        return results


def delete_model(modelID):  # noqa: E501
    """Delete a Model

     # noqa: E501

    :param modelID: ID of Model
    :type modelID: int

    :rtype: None
    """
    results = _globals.orm.delete(
        'Models', 
        clause=f'WHERE modelID={modelID}'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def get_model_by_id(modelID):  # noqa: E501
    """Get a model version by modelID

     # noqa: E501

    :param modelID: ID of Model
    :type modelID: int

    :rtype: List[Model]
    """
    results = _globals.orm.get(
        'Models', 
        clause=f'WHERE modelID={modelID}'
    ) 
    if type(results) != list:
        results = str(results)
    return {'Model':results}


def get_models():  # noqa: E501
    """Get all Models

     # noqa: E501


    :rtype: List[Model]
    """
    results = _globals.orm.get(
        'Models', 
    ) 
    if type(results) != list:
        results = str(results)
    return {'Models':results}


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
        results = _globals.orm.update(
            'Models',
            Model,
            clause=f'WHERE modelID={modelID}'
        ) 
        if type(results) != list:
            results = str(results)
        return results