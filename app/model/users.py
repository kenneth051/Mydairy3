"""users file"""
import datetime
from flask import jsonify
from flask_jwt_extended import create_access_token
from app.database import Database


class UserData(Database):
    """class for implementing user data"""

    def __init__(self):
        """user class constructor"""
        Database.__init__(self)

    def create_user(self, firstname1, lastname1, username1,
                    password1, gender1):
        """method for creating a user"""
        try:
            response = ""
            cur = self.con.cursor()
            cur.execute("""SELECT username FROM Users where
                        username =%s """, (username1, ))
            self.con.commit()
            result = cur.rowcount
            if result > 0:
                response = jsonify({"message": "username is already used"})
                response.status_code = 409
            else:
                cur.execute("""INSERT INTO Users(firstname, lastname, username,
                            password,gender)VALUES (%s, %s, %s, %s, %s)""",
                            (firstname1, lastname1, username1, password1,
                             gender1))
                self.con.commit()
                response = jsonify({"message": "registeration successfuly"})
                response.status_code = 201
            return response
        except:
            response = jsonify({"message": "user cannot be registered"})
            response.status_code = 400
            return response

    def login(self, username1, password1):
        """method for loging in a user"""
        try:
            response = ""
            cur = self.con.cursor()
            cur.execute("""SELECT * FROM  Users where username = %s AND
                        password = %s""", (username1, password1))
            self.con.commit()
            count = cur.rowcount
            result = cur.fetchone()
            if count > 0:
                expires = datetime.timedelta(days=1)
                loggedin_user = dict(user_id=result[0], firstname=result[1],
                                     lastname=result[2], username=result[3])
                access_token = create_access_token(identity=loggedin_user,
                                                   expires_delta=expires)
                response = jsonify({"message": "You are logged in",
                                    "token": access_token})
                response.status_code = 200
            else:
                response = jsonify({"message": "Invalid username or password"})
                response.status_code = 403
            return response
        except:
            return jsonify({"message": "login failure contact ADMIN"})
