#!/usr/bin/python3
"""
This module contains a new view for Review instance
"""
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from api.v1.app import page_not_found
from models import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'])
def get_place_rev(place_id):
    """
    Retrieves list of all Review objects and creates an instance as well
    """
    place = storage.get("Place", place_id)

    if place is None:
        abort(404)

    if request.method == 'GET':
        return jsonify([obj.to_dict() for obj in storage.all("Review").values()
                        if obj.place_id == place_id])

    if request.method == 'POST':
        if not request.json:
            abort(400, 'Not a JSON')
        if 'user_id' not in request.json:
            abort(400, 'Missing user_id')
        if 'text' not in request.json:
            abort(400, 'Missing text')
        data = request.get_json().get('text')
        id = request.get_json().get('user_id')
        user = storage.get('User', user_id)
        if user is not None:
            abort(404)
        new_review = City(user_id=user_id, text=data, place_id=place_id)
        new_review.save()
        return make_response(jsonify(new_review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'])
def update_review(review_id):
    """
    Performs certain functions on a review instance
    if the action cannot be performed, a 404 error is displayed
    """
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)

    if request.method == 'GET':
        data = review.to_dict()
        return make_response(jsonify(data), 200)

    elif request.method == 'DELETE':
        data = {}
        storage.delete(review)
        storage.save()
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    elif request.method == 'PUT':
        if not request.json:
            abort(400, 'Not a JSON')
        for k, v in request.json.items():
            if k not in ['updated_at', 'created_at', 'id',
                         'user_id', 'place_id']:
                setattr(review, k, v)
        review.save()
        data = city.to_dict()
        return make_response(jsonify(data), 200)
