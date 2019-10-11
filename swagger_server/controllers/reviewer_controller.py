import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.reviewer import Reviewer  # noqa: E501
from swagger_server import util


def add_reviewer(reviewer):  # noqa: E501
    """Add a Reviewer

     # noqa: E501

    :param reviewer: Reviewer to be added
    :type reviewer: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        reviewer = Reviewer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_reviewer(reviewerID):  # noqa: E501
    """Delete a Reviewer

     # noqa: E501

    :param reviewerID: ID of Reviewer
    :type reviewerID: int

    :rtype: None
    """
    return 'do some magic!'


def get_reviewer_by_id(reviewerID):  # noqa: E501
    """Get a Reviewer by ID

     # noqa: E501

    :param reviewerID: ID of Reviewer
    :type reviewerID: int

    :rtype: List[Reviewer]
    """
    return 'do some magic!'


def get_reviewers():  # noqa: E501
    """Get all Reviewers

     # noqa: E501


    :rtype: List[Reviewer]
    """
    return 'do some magic!'


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
        reviewer = Reviewer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
