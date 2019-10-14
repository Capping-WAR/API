import connexion
import six

from swagger_server.models.people_review import PeopleReview  # noqa: E501
from swagger_server.models.request_info import RequestInfo  # noqa: E501
from swagger_server import util

from swagger_server.__globals__ import _globals


def add_people_review(people_review):  # noqa: E501
    """Add a People Review

     # noqa: E501

    :param people_review: People Review to be added
    :type people_review: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        values = list(people_review.values())
        cols = ','.join(list(people_review.keys()))
        results =  _globals.orm.insert('PeopleReviews', values, cols=cols)
        if type(results) != list:
            results = str(results)
            
        return results


def delete_people_review(sentenceID):  # noqa: E501
    """Delete a People Review

     # noqa: E501

    :param sentenceID: ID of sentence
    :type sentenceID: int

    :rtype: None
    """
    results = _globals.orm.delete(
        'PeopleReviews', 
        clause=f'WHERE sentenceID={sentenceID}'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def get_people_review_by_id(sentenceID):  # noqa: E501
    """Get a People Review by ID

     # noqa: E501

    :param sentenceID: ID of Sentence
    :type sentenceID: int

    :rtype: List[PeopleReview]
    """
    results = _globals.orm.get(
        'PeopleReviews', 
        clause=f'WHERE sentenceID={sentenceID}'
    ) 
    if type(results) != list:
        results = str(results)
    return results


def get_people_reviews():  # noqa: E501
    """Get all People Reviews

     # noqa: E501


    :rtype: List[PeopleReview]
    """
    results = _globals.orm.get(
        'PeopleReviews', 
    ) 
    if type(results) != list:
        results = str(results)
    return results


def update_people_review(sentenceID, people_review):  # noqa: E501
    """Update a People Review

     # noqa: E501

    :param sentenceID: ID of sentence
    :type sentenceID: int
    :param people_review: New Version of the People Review
    :type people_review: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        results = _globals.orm.update(
            'PeopleReviews',
            people_review,
            clause=f'WHERE sentenceID={sentenceID}'
        ) 
        if type(results) != list:
            results = str(results)
        return results