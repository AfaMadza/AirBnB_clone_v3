#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: display "Hello HBNB!"
"""
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
import os


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def tear_down(self):
    """Teardown application"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """ 404 Not found response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """Parameters to run app"""
    hosts = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    ports = int(os.getenv('HBNB_API_PORT', default=5000))
    app.run(host=hosts, port=ports, threaded=True)
