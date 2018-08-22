#!/usr/bin/python3
"""
This module contains a new view for State instance
"""
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from api.v1.app import not_found
from models import Amenity


@app_views.route('/amenities', methods=['GET', 'POST'])
def get_post_amenities():
    """
    Retrieves list of all Amenity objects
    """
    if request.method == 'GET':
        return jsonify([obj.to_dict()
                        for obj in storage.all("Amenity").values()])
    if request.method == 'POST':
        if not request.json:
            abort(400, 'Not a JSON')
        if 'name' not in request.json:
            abort(400, 'Missing name')
        data = request.get_json().get('name')
        new_amenity = Amenity(name=data)
        new_amenity.save()
        return make_response(jsonify(new_amenity.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'DELETE', 'PUT'])
def update_amenity(amenity_id):
    """
    Performs certain functions on an amenity instance
    if the action cannot be performed, a 404 error is displayed
    """
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)

    if request.method == 'GET':
        data = amenity.to_dict()
        return make_response(jsonify(data), 200)

    elif request.method == 'DELETE':
        data = {}
        storage.delete(amenity)
        storage.save()
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    elif request.method == 'PUT':
        if not request.json:
            abort(400, 'Not a JSON')
        for k, v in request.json.items():
            if k not in ['updated_at', 'created_at', 'id']:
                setattr(amenity, k, v)
        amenity.save()
        data = amenity.to_dict()
        return make_response(jsonify(data), 200)
