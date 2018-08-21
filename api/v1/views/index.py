#!/usr/bin/python3
"""
This module contains a route that returns the status of an object
"""
from api.v1.views import app_views
from flask import Response, jsonify
from models import storage


@app_views.route('/status')
def index():
    """
    Returns a JSON representation of status
    """
    data = {
        "status": "OK"
    }
    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app_views.route('/api/v1/stats')
def count_objects():
    """
    Retrieves number of objects by type
    """
    amenities = storage.count('Amenity')
    cities = storage.count('City')
    places = storage.count('Place')
    reviews = storage.count('Review')
    states = storage.count('State')
    users = storage.count('User')

    data = {
        "amenities": amenities,
        "cities": cities,
        "places": places,
        "reviews": reviews,
        "states": states,
        "users": users
    }

    resp = jasonify(data)
    resp.status_code = 200
    return resp
