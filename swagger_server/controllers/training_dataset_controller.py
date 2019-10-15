import connexion
import six

from swagger_server.models.data_entry import DataEntry  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals

def add_data_entry(dataEntry):  # noqa: E501
    """Add a Data Entry

     # noqa: E501

    :param dataEntry: dataEntry to be added
    :type dataEntry: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        values = list(dataEntry.values())
        cols = ','.join(list(dataEntry.keys()))
        results =  _globals.orm.insert('TrainingDataset', values, cols=cols)
        if type(results) != list:
            results = str(results)
            
        return results


def delete_data_entry(sentenceID):  # noqa: E501
    """Delete a Data Entry

     # noqa: E501

    :param sentenceID: sentenceID of Data Entry
    :type sentenceID: int

    :rtype: None
    """
    results = _globals.orm.delete(
        'TrainingDataset', 
        clause=f'WHERE sentenceID={sentenceID}'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def get_data_entry_by_id(sentenceID):  # noqa: E501
    """Get a Data Entry by ID

     # noqa: E501

    :param sentenceID: sentenceID of Data Entry
    :type sentenceID: int

    :rtype: List[DataEntry]
    """
    results = _globals.orm.get(
        'TrainingDataset', 
        clause=f'WHERE sentenceID={sentenceID}'
    ) 
    if type(results) != list:
        results = str(results)
    return {'DataEntry':results}


def get_data_entrys():  # noqa: E501
    """Get all Data Entries

     # noqa: E501


    :rtype: List[DataEntry]
    """
    results = _globals.orm.get(
        'TrainingDataset', 
    ) 
    if type(results) != list:
        results = str(results)
    return {'DataEntries':results}


def update_data_entry(sentenceID, dataEntry):  # noqa: E501
    """Update a Data Entry

     # noqa: E501

    :param sentenceID: sentenceID of Data Entry
    :type sentenceID: int
    :param dataEntry: New Version of the Data Entry
    :type dataEntry: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        results = _globals.orm.update(
            'TrainingDataset',
            dataEntry,
            clause=f'WHERE sentenceID={sentenceID}'
        )
        if type(results) != list:
            results = str(results)
        return results
