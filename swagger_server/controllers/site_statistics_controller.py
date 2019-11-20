import connexion
import datetime
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
    review_count = _globals.pgapi.get(
        'PeopleReviews',
        cols=' COUNT(*)', # <- the space is meant to be there...
        clause="WHERE dateAdded > current_timestamp - interval '1 days'"
    )[0][0]

    current_day = _globals.pgapi.get(
        'loginStatistics', 
        clause=f"""
            WHERE dayDate >= '{datetime.datetime.now().date()}'::date 
            AND dayDate < ('{datetime.datetime.now().date()}'::date + '1 day'::interval)
        """
    )

    results = None
    # check if todays date is already one of the days in the table
    if len(current_day) is 0:
        # get the oldest date
        oldest_entry = _globals.pgapi.get(
            'loginStatistics', 
            cols=' dateID',
            clause=f"""
                ORDER BY dayDate asc
                LIMIT 1;
                """
        )[0][0]
        
        results = _globals.pgapi.update(
            'loginStatistics', 
            values={
                'dayDate': 'now()',
                'loginCount': 1,
                'reviewCount': review_count
            }, 
            clause=f"WHERE dateID={oldest_entry}"
        )
    else:
        (dateID, dayDate, loginCount,
        reviewCount) = current_day[0]

        results = _globals.pgapi.update(
            'loginStatistics', 
            values={
                'loginCount':loginCount+1,
                'reviewCount': review_count
            }, 
            clause=f"WHERE dateID={dateID}"
        )

    if type(results) != list:
        results = str(results)
    return results


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

    
