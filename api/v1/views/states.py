#!/usr/bin/python3
"""
This module contains a new view for State instance
"""
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from api.v1.app import not_found
from models import State


@app_views.route('/states/', methods=['GET', 'POST'])
def get_states():
    """
    Retrieves list of all State objects
    """
    if request.method == 'GET':
        return jsonify([obj.to_dict()
                        for obj in storage.all("State").values()])
    if request.method == 'POST':
        if not request.json:
            abort(400, 'Not a JSON')
        if 'name' not in request.json:
            abort(400, 'Missing name')
        data = request.get_json().get('name')
        new_state = State(name=data)
        new_state.save()
        return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def update_state(state_id):
    """
    Performs certain functions on a state instance
    if the action cannot be performed, a 404 error is displayed
    """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)

    if request.method == 'GET':
        data = state.to_dict()
        return make_response(jsonify(data), 200)
        # try:
        # return jsonify([obj.to_dict() for obj in storage.all("State").values(state_id)])
       # except:
        #    abort(404)

    elif request.method == 'DELETE':
        data = {}
        # state = storage.get("State", state_id)
        storage.delete(state)
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
        state.save()
        data = state.to_dict()
        return make_response(jsonify(data), 200)
