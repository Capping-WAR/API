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
        values = list(Rule.values())
        cols = ','.join(list(Rule.keys()))
        results =  _globals.pgapi.insert('ModelReviews', values, cols=cols)
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
    results = _globals.pgapi.delete(
        'ModelReviews', 
        clause=f'WHERE sentenceID={sentenceID}'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def get_model_review_by_id(sentenceID):  # noqa: E501
    """Get a Rule by sentenceID

     # noqa: E501

    :param sentenceID: sentence ID of review
    :type sentenceID: int

    :rtype: List[ModelReview]
    """
    results = _globals.pgapi.get(
        'ModelReviews', 
        clause=f'WHERE sentenceID={sentenceID}'
    ) 
    if type(results) != list:
        results = str(results)
    return {'ModelReview':results}


def get_model_reviews():  # noqa: E501
    """Get all Model Reviews

     # noqa: E501


    :rtype: List[ModelReview]
    """
    results = _globals.pgapi.get(
        'ModelReviews', 
    ) 
    if type(results) != list:
        results = str(results)
    return {'ModelReviews':results}


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
        results = _globals.pgapi.update(
            'ModelReviews',
            Model_Review,
            clause=f'WHERE sentenceID={sentenceID}'
        ) 
        if type(results) != list:
            results = str(results)
        return results