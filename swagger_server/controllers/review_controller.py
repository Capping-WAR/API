import connexion
import six

from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.review import Review  # noqa: E501
from swagger_server import util


def add_review(survey):  # noqa: E501
    """Add a Review

     # noqa: E501

    :param survey: Review to be added
    :type survey: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        survey = Review.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_review(reviewID):  # noqa: E501
    """Delete a Review

     # noqa: E501

    :param reviewID: ID of Review
    :type reviewID: str

    :rtype: None
    """
    return 'do some magic!'


def get_review_by_id(reviewID):  # noqa: E501
    """Get a Review by ID

     # noqa: E501

    :param reviewID: ID of Review
    :type reviewID: str

    :rtype: List[Review]
    """
    return 'do some magic!'


def get_reviews():  # noqa: E501
    """Get all Reviews

     # noqa: E501


    :rtype: List[Review]
    """
    return 'do some magic!'


def update_review(reviewID, survey):  # noqa: E501
    """Update a Review

     # noqa: E501

    :param reviewID: ID of Review
    :type reviewID: str
    :param survey: New Version of the Review
    :type survey: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        survey = Review.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
