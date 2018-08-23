#!/usr/bin/python3
"""
This module contains a new view for User instance
"""
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from models import User


@app_views.route('/users', methods=['GET', 'POST'])
def get_users():
    """
    Retrieves list of all User objects
    """
    if request.method == 'GET':
        return jsonify([obj.to_dict() for obj in
                        storage.all("User").values()])
    if request.method == 'POST':
        if not request.json:
            abort(400, 'Not a JSON')
        if 'email' not in request.json:
            abort(400, 'Missing email')
        if 'password' not in request.json:
            abort(400, 'Missing password')
        first = request.get_json().get('first_name')
        last = request.get_json().get('last_name')
        email = request.get_json().get('email')
        pw = request.get_json().get('password')
        new_user = User(first_name=first, last_name=last, email=email,
                        password=pw)
        new_user.save()
        return make_response(jsonify(new_user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'])
def update_user(user_id):
    """
    Performs certain functions on a city instance
    if the action cannot be performed, a 404 error is displayed
    """
    user = storage.get("User", user_id)
    if user is None:
        abort(404)

    if request.method == 'GET':
        data = user.to_dict()
        return make_response(jsonify(data), 200)

    elif request.method == 'DELETE':
        data = {}
        storage.delete(user)
        storage.save()
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    elif request.method == 'PUT':
        if not request.json:
            abort(400, 'Not a JSON')
        for k, v in request.json.items():
            if k not in ['updated_at', 'created_at', 'id', 'email']:
                setattr(user, k, v)
        user.save()
        data = user.to_dict()
        return make_response(jsonify(data), 200)
