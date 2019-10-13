import connexion
import six

from swagger_server.models.model_review import ModelReview  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server.models.rule import Rule  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals


def add_model_review(model_review):  # noqa: E501
    """Add a Model Review

     # noqa: E501

    :param model_review: Model Review to be added
    :type model_review: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        values = list(model_review.values())
        results = _globals.orm.insert('ModelReviews', values)
        if type(results) != list:
            results = str(results)

        return results


def delete_model_review(sentenceID):  # noqa: E501
    """Delete a Model Review

     # noqa: E501

    :param sentenceID: sentence ID of review
    :type sentenceID: int

    :rtype: None
    """
    return _globals.orm.delete(
        'ModelReviews', 
        f'WHERE sentenceID={sentenceID}'
    )


def get_model_review_by_id(sentenceID):  # noqa: E501
    """Get a Rule by sentenceID

     # noqa: E501

    :param sentenceID: sentence ID of review
    :type sentenceID: int

    :rtype: List[ModelReview]
    """
    return _globals.orm.get(
        'ModelReviews', 
        f'WHERE sentenceID={sentenceID}'
    ) 


def get_model_reviews():  # noqa: E501
    """Get all Model Reviews

     # noqa: E501


    :rtype: List[ModelReview]
    """

    return _globals.orm.get('ModelReviews')


def update_model_review(sentenceID, Model_Review):  # noqa: E501
    """Update a Model Review

     # noqa: E501

    :param sentenceID: sentence ID of review
    :type sentenceID: int
    :param Model_Review: Updated Rule
    :type Model_Review: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Model_Review = Rule.from_dict(connexion.request.get_json())  # noqa: E501
    
    return _globals.orm.update(
        'ModelReviews',
        Model_Review
    ) 