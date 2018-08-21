#!/usr/bin/python3
"""
This module contains a new view for State
"""
from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models import storage
from api.v1.app import not_found


@app_views.route('/states', methods=['GET'])
def get_states():
    """
    Retrieves list of all State objects
    """
    return (jsonify(storage.get("State")))

@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def update_state(state_id):
    """
    Retrieves state by state id
    """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)

    if request.method == 'GET':
        data = state.to_dict()
        return make_response(jsonify(data), 200)

    elif request.method == 'DELETE':
        data = {}
        state = get_state(state_id)
        storage.delete(state)
        storage.save()
        resp = jsonify(data)
        resp.staus_code = 200
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
