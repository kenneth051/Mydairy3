"""api views"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.model.diary import Diary
from app.model.users import UserData
from app.validation_main import Validate2

ROUTES = Blueprint('routes', __name__)


@ROUTES.route('/API/v1/auth/user/signup', methods=['POST'])
def register():
    """ view to register a user """
    try:
        data = request.get_json()
        info = Validate2.validate_user(data["username"], data["firstname"],
                                       data["lastname"], data["email"],
                                       data["password"],
                                       data["gender"])
        if info is True:
            obj = UserData()
            result = obj.create_user(data["firstname"], data["lastname"],
                                     data["username"], data["email"], data["password"],
                                     data["gender"])
            return result
        else:
            response = jsonify({"message": info})
            response.status_code = 400
            return response
    except:
        return jsonify({"Error": "Missing or invalid input field"})


@ROUTES.route('/API/v1/auth/users/login', methods=['POST'])
def login():
    """view for logging in"""
    try:
        data = request.get_json()
        info = Validate2.validate_login(data["username"], data["password"])
        if info is True:
            obj = UserData()
            info = obj.login(data["username"], data["password"])
            return info
        else:
            response = jsonify({"message": """Bad username or empty
                                password field"""})
            response.status_code = 400
            return response
    except:
        return jsonify({"Error": "Missing or invalid input field"})


@ROUTES.route('/API/v1/entries', methods=['POST'])
@jwt_required
def create_entry():
    """view to create entries"""
    try:
        data = request.get_json()
        active_user = get_jwt_identity()
        data["user_id"] = active_user["user_id"]
        valid = Validate2(data["title"], data["body"])
        result = valid.validate_empty()
        if result is True:
            obj = Diary()
            info = obj.creating_entry(data["title"], data["body"],
                                      data["user_id"])
            return info
        else:
            response = jsonify({"message": "Invalid data in body or title"})
            response.status_code = 400
            return response
    except:
        response = jsonify({"Error": "Missing or invalid input field"})
        response.status_code = 400
        return response


@ROUTES.route('/API/v1/entries', methods=['GET'])
@jwt_required
def get_entries():
    """view to get entries"""
    active_user = get_jwt_identity()
    user = active_user["user_id"]
    data = Diary()
    info = data.all_entries(user)
    return info


@ROUTES.route('/API/v1/entries/<int:entryid>', methods=['GET'])
@jwt_required
def get_entry(entryid):
    """view to get one entry"""
    active_user = get_jwt_identity()
    user = active_user["user_id"]
    data = Diary()
    info = data.single_entry(entryid, user)
    return info


@ROUTES.route('/API/v1/entries/<int:entryid>', methods=['PUT'])
@jwt_required
def update_entry(entryid):
    """view to update an entry"""
    try:
        active_user = get_jwt_identity()
        user = active_user["user_id"]
        updating_data = request.get_json()
        obj = Validate2(updating_data["title"], updating_data["body"])
        result = obj.validate_empty()
        if result is True:
            data = Diary()
            info = data.update_entry(entryid, user, updating_data["title"],
                                     updating_data["body"])
            return info
        else:
            response = jsonify({"message": "Invalid data in body or title"})
            response.status_code = 400
            return response
    except:
        response = jsonify({"Error": "Missing or invalid input field"})
        response.status_code = 400
        return response
