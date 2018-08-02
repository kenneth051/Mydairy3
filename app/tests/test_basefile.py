""" test base page"""
import unittest
import json
from flask_jwt_extended import create_access_token
from app import APP
from app.database import Database


class TestBase(unittest.TestCase):
    """class to test our api"""
    create_user = json.dumps(dict(firstname="joy", lastname="williams",
                                  username="home", email="ken@gmail.com",
                                  password="1234567890", gender="female"))
    duplicate_user = json.dumps(dict(firstname="joy", lastname="williams",
                                     username="joy", email="ken@ken.com",
                                     password="1234567890", gender="female"))
    invaliduser = json.dumps(dict(firstname="joy", lastname="williams",
                                  username="***", email="ken@ken.com",
                                  password="1234567890", gender="female"))
    invalid_email = json.dumps(dict(firstname="joy", lastname="williams",
                                    username="home", email="ken.com",
                                    password="1234567890", gender="female"))
    invaliduser1 = json.dumps(dict(firstname="****", lastname="   ",
                                   username="andela", email="ken@ken.com",
                                   password="1234567890", gender="female"))
    invalidpassword = json.dumps(dict(firstname="uuuuu", lastname="yyyyyyy",
                                      username="andela", email="ken@ken.com",
                                      password="    ", gender="female"))
    passwordlength = json.dumps(dict(firstname="uuuuu", lastname="yyyyyyy",
                                     username="andela", email="ken@ken.com",
                                     password="uuuuu", gender="female"))
    logindata = json.dumps(dict(username="joy", password="12345678"))
    login_validation = json.dumps(dict(username="******", password="12345678"))
    create_entry = json.dumps(dict(title="kampala", body="this is my body",
                                   user_id=1))
    duplicate_entry = json.dumps(dict(title="Testing", body="testing data",
                                      user_id=1))
    update_entry = json.dumps(dict(title="war", body="We will be fine",
                                   user_id=1))
    duplicate_update = json.dumps(dict(title="Testing",
                                       body="We will be fine", user_id=1))

    def setUp(self):
        """Define test variables and initialize app."""
        APP.config['TESTING'] = True
        self.app = APP
        with APP.test_request_context():
            self.loggedin_user = dict(user_id=1, firstname='Dumba',
                                      lastname='kenneth', username='joy')
            self.access_token = create_access_token(self.loggedin_user)
            self.access_header = {'Authorization': 'Bearer {}'.format(
                self.access_token)}

    def tearDown(self):
        users_table = ("""DROP TABLE IF EXISTS users CASCADE;""")
        entries_table = ("""DROP TABLE IF EXISTS entries CASCADE;""")
        con = Database.testing_db_teardown()
        cur = con.cursor()
        cur.execute(users_table)
        con.commit()
        cur.execute(entries_table)
        con.commit()

if __name__ == '__main__':
    unittest.main()
