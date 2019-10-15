import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.reviewer import Reviewer  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals

def add_reviewer(reviewer):  # noqa: E501
    """Add a Reviewer

     # noqa: E501

    :param reviewer: Reviewer to be added
    :type reviewer: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        values = list(reviewer.values())
        cols = ','.join(list(reviewer.keys()))
        results =  _globals.orm.insert('Reviewers', values, cols=cols)
        if type(results) != list:
            results = str(results)
            
        return results


def delete_reviewer(reviewerID):  # noqa: E501
    """Delete a Reviewer

     # noqa: E501

    :param reviewerID: ID of Reviewer
    :type reviewerID: int

    :rtype: None
    """
    results = _globals.orm.delete(
        'Reviewers', 
        clause=f'WHERE reviewerID={reviewerID}'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def get_reviewer_by_id(reviewerID):  # noqa: E501
    """Get a Reviewer by ID

     # noqa: E501

    :param reviewerID: ID of Reviewer
    :type reviewerID: int

    :rtype: List[Reviewer]
    """
    results = _globals.orm.get(
        'Reviewers', 
        clause=f'WHERE reviewerID={reviewerID}'
    ) 
    if type(results) != list:
        results = str(results)
    return {'Reviewer':results}



def get_reviewers():  # noqa: E501
    """Get all Reviewers

     # noqa: E501


    :rtype: List[Reviewer]
    """
    results = _globals.orm.get(
        'Reviewers', 
    ) 
    if type(results) != list:
        results = str(results)
    return {'Reviewers':results}


def update_reviewer(reviewerID, reviewer):  # noqa: E501
    """Update a Reviewer

     # noqa: E501

    :param reviewerID: ID of Reviewer
    :type reviewerID: int
    :param reviewer: New Version of the Reviewer
    :type reviewer: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        results = _globals.orm.update(
            'Reviewers',
            reviewer,
            clause=f'WHERE reviewerID={reviewerID}'
        ) 
        if type(results) != list:
            results = str(results)
        return results
