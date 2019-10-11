import connexion
import six

from swagger_server.models.data_entry import DataEntry  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server import util


def add_data_entry(dataEntry):  # noqa: E501
    """Add a Data Entry

     # noqa: E501

    :param dataEntry: dataEntry to be added
    :type dataEntry: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dataEntry = DataEntry.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_data_entry(ID):  # noqa: E501
    """Delete a Data Entry

     # noqa: E501

    :param ID: ID of Data Entry
    :type ID: int

    :rtype: None
    """
    return 'do some magic!'


def get_data_entry_by_id(ID):  # noqa: E501
    """Get a Data Entry by ID

     # noqa: E501

    :param ID: ID of Data Entry
    :type ID: int

    :rtype: List[DataEntry]
    """
    return 'do some magic!'


def get_data_entrys():  # noqa: E501
    """Get all Data Entries

     # noqa: E501


    :rtype: List[DataEntry]
    """
    return 'do some magic!'


def update_data_entry(ID, dataEntry):  # noqa: E501
    """Update a Data Entry

     # noqa: E501

    :param ID: ID of Data Entry
    :type ID: int
    :param dataEntry: New Version of the Data Entry
    :type dataEntry: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dataEntry = DataEntry.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
