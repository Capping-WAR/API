import connexion
import six

from swagger_server.models.query import Query  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server import util


def get_search_results():  # noqa: E501
    """Runs a given SELECT Query

     # noqa: E501


    :rtype: Query
    """
    return 'do some magic!'
