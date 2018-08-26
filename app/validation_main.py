"""validation class with regular expressions"""
import re
from app.validation_functions import validate_userfields, validate_username


class Validate2():
    """valiation class for diary inputs"""
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def validate_empty(self):
        """method to validate my input """
        result = ""
        title_empty = Validate2.validate_names(self.title)
        if title_empty is False:
            result = "title cannot be empty"
        elif not re.search("[a-zA-Z0-9]", self.title):
            result = "title can only have alphanumeric characters"
        elif not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", self.body):
            result = "body cannot be empty"
        else:
            result = True
        return result
    @classmethod
    def validate_names(cls,name):
        result =""
        if not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", name):
            result = False
        else:
            result = True
        return result                          

    @classmethod
    def validate_user(cls, username, firstname, lastname, email, password, gender):
        """method to validate user regiteration"""
        response = ""
        password_length = len(password)
        username1 = validate_username(username)
        username2 = Validate2.validate_names(username)
        firstname1 = validate_userfields(firstname)
        lastname1 = validate_userfields(lastname)
        firstname2 = Validate2.validate_names(firstname)
        lastname2 = Validate2.validate_names(lastname)
        gender = str(gender)
        gender = gender.lower()
        if username2 is False:
            response = "Username cannot be empty"
        elif username1 is False:
            response = "username can only have alphanumeric characters"
        elif firstname2 is False:
            response = "Firstname cannot be empty"
        elif lastname2 is False:
            response = "lastname cannot be empty"
        elif firstname1 is False:
            response = "Invalid firstname use alphabets only"
        elif lastname1 is False:
            response = "Invalid lastname, use aphabets only"    
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
            response = "username can only have alphanumeric characters"
        elif not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", password):
            response = "invalid password data"
        else:
            response = True
        return response
