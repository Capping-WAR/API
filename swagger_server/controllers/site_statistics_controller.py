import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server import util


def post_login_stats():  # noqa: E501
    """updates current login statistics count

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def post_user_stats(user_info):  # noqa: E501
    """updates current user statistics count

     # noqa: E501

    :param user_info: Which os and platform is the user on.
    :type user_info: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_info = UserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
