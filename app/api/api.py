"""api views"""
from app import APP
from flask import Blueprint,request, jsonify
from app.model.diary import Diary
from app.model.users import UserData
from app.validation2 import Validate2

routes= Blueprint('routes', __name__)

@routes.route('/API/v1/auth/users', methods=['POST'])
def register():
    """ a user can create a ride here """
    try:
        data = request.get_json()
        obj  = UserData()
        result=obj.create_user(data["firstname"], data["lastname"],
                                data["username"], data["password"],
                                data["gender"])
        return result
    except:
        return jsonify({"result":"Error with what your sending"})



@routes.route('/API/v1/entries', methods=['POST'])
def create_entry():
    """method to create entries"""
    try:
        data = request.get_json()
        valid = Validate2(data["title"], data["body"])
        info = valid.validate_empty()
        if info is True:
            obj=Diary()
            info = obj.creating_entry(data["title"], data["body"], data["user_id"])
            return info
        else:
            response = jsonify({"message": info})
            response.status_code = 400
            return response
    except:
        response = jsonify({"message": "DATA FIELDS ISSUE"})
        response.status_code = 400
        return response


@routes.route('/API/v1/entries', methods=['GET'])
def get_entries():
    """method to get entries"""
    data = Diary()
    info=data.all_entries()
    return info


@routes.route('/API/v1/entries/<int:entryid>', methods=['GET'])
def get_entry(entryid):
    """method to get one entry"""
    data=Diary()
    info=data.single_entry(entryid)
    return info


@routes.route('/API/v1/entries/<int:entryid>', methods=['PUT'])
def update_entry(entryid):
    """method to update an entry"""
    pass

