import connexion
import six

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
    if 'select' not in q.lower():
        return {
            'message':'query must be a select'
        }
    else:
        results = _globals.orm._query(q) 
        if type(results) != list:
            results = str(results)
        return results
