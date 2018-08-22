#!/usr/bin/python3
"""
This module contains a new view for State instance
"""
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from api.v1.app import not_found
from models import City
from models import State

@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def get_cities(state_id):
    """
    Retrieves list of all City objects
    """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if request.method == 'GET':
        return jsonify([obj.to_dict() for obj in
                        storage.all("City").values() if obj.state_id == state_id])
    if request.method == 'POST':
        if not request.json:
            abort(400, 'Not a JSON')
        if 'name' not in request.json:
            abort(400, 'Missing name')
        data = request.get_json().get('name')
        new_city = City(name=data)
        new_city.save()
        return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'])
def update_city(city_id):
    """
    Performs certain functions on a city instance
    if the action cannot be performed, a 404 error is displayed
    """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)

    if request.method == 'GET':
        data = city.to_dict()
        return make_response(jsonify(data), 200)

    elif request.method == 'DELETE':
        data = {}
        storage.delete(city)
        storage.save()
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    elif request.method == 'PUT':
        if not request.json:
            abort(400, 'Not a JSON')
        for k, v in request.json.items():
            if k not in ['updated_at', 'created_at', 'id']:
                setattr(state, k, v)
        city.save()
        data = city.to_dict()
        return make_response(jsonify(data), 200)
