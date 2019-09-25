import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.version import Version  # noqa: E501
from swagger_server import util


def add_version(Version):  # noqa: E501
    """Add a Version

     # noqa: E501

    :param Version: Version to be added
    :type Version: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Version = Version.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_version(modelID):  # noqa: E501
    """Delete a Version

     # noqa: E501

    :param modelID: ID of model
    :type modelID: int

    :rtype: None
    """
    return 'do some magic!'


def get_version_by_id(modelID):  # noqa: E501
    """Get a model version by modelID

     # noqa: E501

    :param modelID: ID of Model
    :type modelID: int

    :rtype: List[Version]
    """
    return 'do some magic!'


def get_versions():  # noqa: E501
    """Get all Versions

     # noqa: E501


    :rtype: List[Version]
    """
    return 'do some magic!'


def update_version(modelID, Version):  # noqa: E501
    """Update a Version

     # noqa: E501

    :param modelID: ID of Model
    :type modelID: int
    :param Version: Updated Version
    :type Version: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Version = Version.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
