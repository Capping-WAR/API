import connexion
import six

from swagger_server.models.query import Query  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server import util


def get_search_results(query):  # noqa: E501
    """Runs a given SELECT Query

     # noqa: E501

    :param query: Query to be run
    :type query: dict | bytes

    :rtype: List[object]
    """
    if connexion.request.is_json:
        query = Query.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
