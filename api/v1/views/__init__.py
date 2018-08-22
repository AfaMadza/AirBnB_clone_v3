#!/usr/bin/python3
"""
Initialization file for views
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.users import *
from api.v1.views.amenities import *
<<<<<<< HEAD
from api.v1.views.places import *
=======
from api.v1.views.reviews import *
>>>>>>> eb31a5f6b79aaf012d444306ae916724250aefed
