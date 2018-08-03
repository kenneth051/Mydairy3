"""API test page"""
from app.tests.test_basefile import TestBase


class UserTesting(TestBase):
    """class to test our api"""

    def test_create_user(self):
        """test creating a new user """
        tester = self.app.test_client(self)
        response = tester.post('/API/v1/auth/user/signup',
                               data=TestBase.create_user,
                               content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"registeration successfuly", response.data)

    def test_duplicate_username(self):
        """test method to check duplication"""
        tester = self.app.test_client(self)
        response = tester.post('/API/v1/auth/user/signup',
                               data=TestBase.duplicate_user,
                               content_type="application/json")
        self.assertEqual(response.status_code, 409)
        self.assertIn(b"username or email is already used",
                      response.data)
            
    def test_invalid_email(self):
        """test method to check duplication"""
        tester = self.app.test_client(self)
        response = tester.post('/API/v1/auth/user/signup',
                               data=TestBase.invalid_email,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Invalid email address",
                      response.data)                  

    def test_username_validation(self):
        """test method for checking username validation"""
        tester = self.app.test_client(self)
        response = tester.post('/API/v1/auth/user/signup',
                               data=TestBase.invaliduser,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Invalid username field data,user alphanumeric",
                      response.data)

    def test__userdata_validation(self):
        """test method to validate firstname and lastname"""
        tester = self.app.test_client(self)
        response = tester.post('/API/v1/auth/user/signup',
                               data=TestBase.invaliduser1,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Invalid firstname or lastname, use alphabets",
                      response.data)

    def test_password_validation(self):
        """test method for password validation"""
        tester = self.app.test_client(self)
        response = tester.post('/API/v1/auth/user/signup',
                               data=TestBase.invalidpassword,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"invalid password data", response.data)

    def test_creating_password_length(self):
        """test method for checking password length"""
        tester = self.app.test_client(self)
        response = tester.post('/API/v1/auth/user/signup',
                               data=TestBase.passwordlength,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Password should be 8 or more characters long",
                      response.data)

    def test_login(self):
        """test method to login a user"""
        tester = self.app.test_client(self)
        res = tester.post('/API/v1/auth/users/login', data=TestBase.logindata,
                          content_type="application/json")
        self.assertEqual(res.status_code, 200)
        print(res.data)

    def test_login_validation(self):
        """test method to check login validation"""
        tester = self.app.test_client(self)
        res = tester.post('/API/v1/auth/users/login',
                          data=TestBase.login_validation,
                          content_type="application/json")
        self.assertEqual(res.status_code, 400)

    def test_for_wrong_url(self):
        """test for wrong url"""
        tester = self.app.test_client(self)
        response = tester.get('/API/v1/iuut',
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)
