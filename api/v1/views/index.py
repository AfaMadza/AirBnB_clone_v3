#!/usr/bin/python3
"""
This module contains a route that returns the status of an object
"""
from api.v1.views import app_views
from flask import Response, jsonify

@app_views.route('/status')
def index():
    """
    Returns a JSON representation of status
    """
    data = { "status": "OK" }
    resp = jsonify(data)
    resp.status_code = 200
    return resp
