"""validation class with regular expressions"""
import re
from app.validation3 import validate_userfields, validate_username


class Validate2():
    """valiation class for diary inputs"""
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def validate_empty(self):
        """method to validate my input """
        result = ""
        if(not re.search("[a-zA-Z0-9]", self.title) or not
           re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", self.body)):
            result = False
        else:
            result = True
        return result

    @classmethod
    def validate_user(cls, username, firstname, lastname, email, password, gender):
        """method to validzte user regiteration"""
        response = ""
        password_length = len(password)
        info = validate_username(username)
        firstname2 = validate_userfields(firstname)
        lastname2 = validate_userfields(lastname)
        gender = str(gender)
        gender = gender.lower()
        if info is False:
            response = "Invalid username field data,user alphanumeric"
        elif firstname2 is False or lastname2 is False:
            response = "Invalid firstname or lastname, use alphabets"
        elif gender not in ("male", "female"):
            response = "Invalid gender, should be male or female"
        elif not re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\\.[a-zA-Z]+$", email):
            response = "Invalid email address"
        elif not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", password):
            response = "invalid password data"
        elif password_length <= 8:
            response = "Password should be 8 or more characters long"
        else:
            response = True
        return response

    @classmethod
    def validate_login(cls, username, password):
        """method to validate user login"""
        response = ""
        info = validate_username(username)
        if info is False:
            response = "Invalid username field data,user alphanumeric"
        elif not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", password):
            response = "invalid password data"
        else:
            response = True
        return response
