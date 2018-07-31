""" test base page"""
import unittest
import json
from flask_jwt_extended import (create_access_token, get_jwt_identity)
from app.api.api import APP
from app.database import Database


class TestBase(unittest.TestCase):
    """class to test our api"""
    def setUp(self):
        """Define test variables and initialize app."""
        APP.config['TESTING'] = True
        self.app = APP                     
        with APP.test_request_context():
            self.loggedin_user=dict(user_id=1,firstname='Dumba',lastname='kenneth',username='joy')
            self.access_token=create_access_token(self.loggedin_user)
            self.access_header={'Authorization':'Bearer {}'.format(self.access_token)}

    def tearDown(self):
            users_table=("""DROP TABLE IF EXISTS users;""")
            entries_table=("""DROP TABLE IF EXISTS "entries";""")
            con = Database.testing_db_teardown()
            cur = con.cursor()
            cur.execute(users_table)
            con.commit()
            cur.execute(entries_table)
            con.commit()

if __name__ == '__main__':
    unittest.main()
