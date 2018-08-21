#!/usr/bin/python3
"""
This module contains a new view for State
"""
from api.v1.views import app_views
from flask import Response, jsonify
from models import storage
from api.v1.app import not_found

@app_views.route('/states', methods = ['GET'])
def get_states():
    """
    Retrieves list of all State objects
    """
    return (jsonify(storage.get("State")))

@app_view.route('/states/<state_id>', methods = ['GET'])
def get_state(state_id):
    """
    Retrieves state by state id
    """
    state = storage.get("State", state_id)
    if state is None:
        return not_found()

@app_view.route('/states/<state_id>', methods = ['DELETE'])
def delete_state(state_id):
    """
    Deletes a state object
    """
    data = {}
    state = get_state(state_id)
    try:
        storage.delete(state)
    except:
        resp = jsonify(data)
        resp.staus_code = 200
        return resp
