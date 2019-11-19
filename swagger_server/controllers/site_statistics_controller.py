import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals


def post_login_stats():  # noqa: E501
    """updates current login statistics count

     # noqa: E501


    :rtype: None
    """
    data = _globals.pgapi.get('userStatistics')
    print(data)
    return 'do some magic!'


def post_user_stats(user_info):  # noqa: E501
    """updates current user statistics count

     # noqa: E501

    :param user_info: Which os and platform is the user on.
    :type user_info: dict | bytes

    :rtype: None
    """
    if user_info is not None:
        (stat_id, windowsCount, macosCount, otherCount, isDesktopCount,
        isMobileCount) = _globals.pgapi.get('userStatistics')[0]

        if user_info['os'] == 'Mac':
            macosCount += 1
        elif user_info['os'] == 'Windows':
            windowsCount += 1
        elif user_info['os'] == 'Other':
            otherCount += 1

        if user_info['platform'] == 'isDesktop':
            isDesktopCount += 1
        elif user_info['platform'] == 'isMobile':
            isMobileCount += 1

        results = _globals.pgapi.update('userStatistics', values={
            'windowsCount': windowsCount,
            'macosCount': macosCount,
            'otherCount': otherCount,
            'isDesktopCount': isDesktopCount,
            'isMobileCount': isMobileCount
            },
            clause=f'WHERE statisticsID=1'
        )

        if type(results) != list:
            results = str(results)
        return results

    else:
        return 'user_info is required', 400

    
