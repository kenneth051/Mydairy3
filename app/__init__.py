from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
APP = Flask(__name__)
APP.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(APP)

from app.api.api import routes
APP.register_blueprint(routes)

@APP.errorhandler(404)
def page_not_found(e):
    """function incase of invalid url"""
    response = jsonify({"message": "USE A VALID URL"})
    response.status_code = 404
    return response
