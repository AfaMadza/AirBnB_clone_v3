#!/usr/bin/python3
"""
This module contains a route that returns the status of an object
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def index():
    """
    Returns a JSON representation of status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
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

    resp = jsonify(data)
    return resp
