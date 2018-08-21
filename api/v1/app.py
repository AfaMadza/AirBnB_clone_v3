#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: display "Hello HBNB!"
"""
from models import storage
from flask import Flask
from api.v1.views import app_views
from Blueprint import register_blueprint


app = Flask(__name__)
app.register_blueprint("app_views", url_prefix="/api/v1")
app.url_map.strict_slashes=False


@app.teardown_appcontext
def tear_down(self):
        """Teardown application"""
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
