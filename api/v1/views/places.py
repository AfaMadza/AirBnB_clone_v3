#!/usr/bin/python3
"""
This module contains a new view for Place instance
"""
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from models import State
from models import City
from models import Place


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'])
def get_places(city_id):
    """
    Retrieves list of all Place objects
    """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    if request.method == 'GET':
        return jsonify([obj.to_dict() for obj in storage.all("Place").values()
                        if obj.city_id == city_id])
    if request.method == 'POST':
        if not request.json:
            abort(400, 'Not a JSON')
        if 'user_id' not in request.json:
            abort(400, 'Missing user_id')
        if storage.get('User', request.json['user_id']) is None:
            abort(404)
        if 'name' not in request.json:
            abort(400, 'Missing name')
        data = Place(**request.get_json())
        data.city_id = city_id
        data.save()
        return make_response(jsonify(data.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['GET', 'DELETE', 'PUT'])
def update_place(place_id):
    """
    Performs certain functions on a place instance
    if the action cannot be performed, a 404 error is displayed
    """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)

    if request.method == 'GET':
        data = place.to_dict()
        return make_response(jsonify(data), 200)

    elif request.method == 'DELETE':
        data = {}
        storage.delete(place)
        storage.save()
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    elif request.method == 'PUT':
        if not request.json:
            abort(400, 'Not a JSON')
        for k, v in request.json.items():
            if k not in ['updated_at', 'created_at', 'user_id',
                         'id', 'city_id']:
                setattr(place, k, v)
        place.save()
        data = place.to_dict()
        return make_response(jsonify(data), 200)
