import connexion
import requests
import base64
import six
import os

from swagger_server.models.query import Query  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals


def get_search_results(query):  # noqa: E501
    """Runs a given SELECT Query

     # noqa: E501

    :param query: Query to be run
    :type query: dict | bytes

    :rtype: List[object]
    """
    q = query['query']
    if 'from' in q.lower():
        table = q.lower().split('from')[1]
        table = table.split(';')[0]
        table = table.split(' ')[1]
        table = table.split('(')[0]
        table = table.split('where')[0]
        table = table.strip()
    if 'call' in q.lower():
        table = q.lower().split('call')[1]
        table = table.split('(')[0].strip()
    if 'select' not in q.lower() and 'call' not in q.lower():
        return {
            'message':'query must be a select'
        }
    else:
        results = _globals.pgapi._query(q) 
        if type(results) != list:
            results = str(results)
        return {table:results}

def get_threads():  # noqa: E501
    """gets all running threads from AI API

     # noqa: E501


    :rtype: None
    """
    url = os.getenv('AI_API_URL')
    return requests.get(f'{url}/threads').json()

def post_retrain():  # noqa: E501
    """checks for new entries in the traning data set 
    table and sends a request to train a new model if one is found

     # noqa: E501


    :rtype: None
    """
    count = _globals.pgapi._query('SELECT COUNT(*) FROM TrainingDataset')[0][0]
    retrain_response = None
    
    if _globals.dataset_count is not None:
        if count != _globals.dataset_count:
            retrain_response = callRetrain()
    else:
        results = _globals.pgapi._query(
            """
            SELECT * 
            FROM TrainingDataset 
            WHERE dateAdded > current_timestamp - interval '1 minutes';
            """
        )
        if len(results) != 0:
            retrain_response = callRetrain()


    _globals.dataset_count = count

    if retrain_response is None:
        return 'No new entries found', 200
    else:
        return retrain_response.json(), 201

def callRetrain():
    url = os.getenv('AI_API_URL')
    username = os.getenv('AI_USER')
    password = os.getenv('AI_PASS')

    return requests.post(
        f'{url}/retrain', 
        auth=(username, password), 
        json={
            'callerID': 'WAR_API'
        }
    )