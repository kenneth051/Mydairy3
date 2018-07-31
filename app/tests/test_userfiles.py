"""API test page"""
import json
from app.tests.test_basefile import TestBase

class UserTesting(TestBase):
    """class to test our api"""

    def test_create_user(self):
        tester=self.app.test_client(self)
        response=tester.post('/API/v1/auth/user/signup',
         data=json.dumps(dict(firstname = "joy",lastname = "williams",username = "williams",
        password="1234567890",gender = "female")),content_type="application/json") 
        self.assertEqual(response.status_code,201) 
        self.assertIn(b"you have successfuly registered", response.data)

    def test_creating_user_with_duplicate_username(self):
        tester=self.app.test_client(self)
        response=tester.post('/API/v1/auth/user/signup',
         data=json.dumps(dict(firstname = "joy",lastname = "williams",username = "joy",
        password="1234567890",gender = "female")),content_type="application/json") 
        self.assertEqual(response.status_code,409) 
        self.assertIn(b"username is  already used, create a unique one", response.data)

    def test_creating_username_validation(self):
        tester=self.app.test_client(self)
        response=tester.post('/API/v1/auth/user/signup',
         data=json.dumps(dict(firstname = "joy",lastname = "williams",username = "***",
        password="1234567890",gender = "female")),content_type="application/json") 
        self.assertEqual(response.status_code,400) 
        self.assertIn(b"Invalid username field data,user alphanumeric", response.data)

    def test_creating_user_data_validation(self):
        tester=self.app.test_client(self)
        response=tester.post('/API/v1/auth/user/signup',
         data=json.dumps(dict(firstname = "****",lastname = "   ",username = "andela",
        password="1234567890",gender = "female")),content_type="application/json") 
        self.assertEqual(response.status_code,400) 
        self.assertIn(b"Invalid firstname or lastname, use alphabets", response.data)

    def test_creating_user_password_validation(self):
        tester=self.app.test_client(self)
        response=tester.post('/API/v1/auth/user/signup',
         data=json.dumps(dict(firstname = "uuuuu",lastname = "yyyyyyy",username = "andela",
        password="    ",gender = "female")),content_type="application/json") 
        self.assertEqual(response.status_code,400) 
        self.assertIn(b"invalid password data", response.data)

    def test_creating_password_length(self):
        tester=self.app.test_client(self)
        response=tester.post('/API/v1/auth/user/signup',
         data=json.dumps(dict(firstname = "uuuuu",lastname = "yyyyyyy",username = "andela",
        password="uuuuu",gender = "female")),content_type="application/json") 
        self.assertEqual(response.status_code,400) 
        self.assertIn(b"Password should be 8 or more characters long", response.data)              

    def test_login(self):  
        tester=self.app.test_client(self)
        res = tester.post('/API/v1/auth/users/login',data = json.dumps(dict(username = "joy",password = "12345678")),
        content_type = "application/json") 
        self.assertEqual(res.status_code,201) 
        print(res.data)    

        def test_for_wrong_url(self):
            """test for wrong url"""
        tester=self.app.test_client(self)
        response = tester.get('/API/v1/iuut',
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)

   

    
