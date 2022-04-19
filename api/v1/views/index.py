#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

app = Flask(__name__)


@app_views.route('/status')
def status():
    return jsonify({
                     "status": "OK"
                   })


@app_views.route('/stats')
def stat():
    class_dict = {"amenities": "Amenity", "cities": "City", "places": "Place",
                  "reviews": "Review", "states": "State", "users": "User"}
    for key in class_dict:
        class_dict[key] = storage.count(class_dict[key])
    return jsonify(class_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
