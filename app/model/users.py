from app.database import Database
from flask import jsonify
class UserData(Database):

    def __init__(self):
        Database.__init__(self)
    def create_user(self, firstname1, lastname1, username1, password1, gender1):
        try:
            cur = self.con.cursor()                   
            cur.execute("SELECT username FROM Users where username =%s ", (username1, ))
            self.con.commit()
            result = cur.rowcount
            if result > 0:
                response = jsonify({"message":"username is  already in used, create a unique one"})
                response.status_code = 409
                return response     
            else: 
                cur.execute("INSERT INTO Users(firstname, lastname, username, password,gender)VALUES (%s, %s, %s, %s, %s)",
                (firstname1, lastname1, username1, password1, gender1))    
                self.con.commit()
                response = jsonify({"message":"you have successfuly registered"})
                response.status_code =201
                return response
        except:
            response = jsonify({"message":"user cannot be registered, contact ADMIN"})
            response.status_code =400
            return response

