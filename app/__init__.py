from flask import Flask, jsonify

APP = Flask(__name__)

from app.api.api import routes
APP.register_blueprint(routes)

@APP.errorhandler(404)
def page_not_found(e):
    """function incase of invalid url"""
    response = jsonify({"message": "USE A VALID URL"})
    response.status_code = 404
    return response

