"""API test page"""
import unittest
import json
from flask_jwt_extended import (create_access_token, get_jwt_identity)
from app.api.api import APP
from app.model.diary import Diary
from app.model.users import UserData
from app.database import Database


class FlaskTesting(unittest.TestCase):
    """class to test our api"""
    def setUp(self):
        """Define test variables and initialize app."""
        APP.config['TESTING'] = True
        self.app = APP                     
        with APP.test_request_context():
            self.loggedin_user=dict(user_id=1,firstname='Dumba',lastname='kenneth',username='joy')
            self.access_token=create_access_token(self.loggedin_user)
            self.access_header={'Authorization':'Bearer {}'.format(self.access_token)}

    def test_create_user(self):
        tester=APP.test_client(self)
        response=tester.post('/API/v1/auth/signup',
         data=json.dumps(dict(firstname = "joy",lastname = "williams",username = "williams",
        password="1234567890",gender = "female")),content_type="application/json") 
        self.assertEqual(response.status_code,201) 
        self.assertIn(b"you have successfuly registered", response.data)

    def test_creating_user_with_duplicate_username(self):
        tester=APP.test_client(self)
        response=tester.post('/API/v1/auth/signup',
         data=json.dumps(dict(firstname = "joy",lastname = "williams",username = "joy",
        password="1234567890",gender = "female")),content_type="application/json") 
        self.assertEqual(response.status_code,409) 
        self.assertIn(b"username is  already used, create a unique one", response.data)
    def test_login(self):  
        tester = APP.test_client(self)
        res = tester.post('/API/v1/auth/users/login',data = json.dumps(dict(username = "joy",password = "12345678")),
        content_type = "application/json") 
        self.assertEqual(res.status_code,201) 
        print(res.data)    

    def test_to_create_entry(self):
        """test to create an entry"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(title="kampala",
                body="this is my body",user_id=1)),headers=self.access_header, content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Entry has been created successfully", res.data)

    def test_to_create_entry_with_duplicate_data(self):
        """test to create an entry"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(title="Testing",
                body="testing data",user_id=1)),headers=self.access_header, content_type='application/json')
        self.assertEqual(res.status_code, 409)
        self.assertIn(b"Entry has been created previously,Duplicate data", res.data)
        
    def test_to_get_all_entries(self):
        """test to get all entries"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries',headers=self.access_header,content_type="application/json")
        self.assertEqual(response.status_code, 200)
    
        def test_for_wrong_url(self):
            """test for wrong url"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/iuut',
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_to_get_single_entry(self):
        """test to get a single entry content"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/1',headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_to_get_single_entry_with_invalid_id(self):
        """test to get a single entry content"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/11111',headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"The URL is invalid ,wrong ID given", response.data)           
   
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
