"""API test page"""
import json
from app.tests.test_basefile import TestBase

class EntryTesting(TestBase):
    """class to test our entries"""

    def test_to_create_entry(self):
        """test to create an entry"""
        tester=self.app.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(title="kampala",
                body="this is my body",user_id=1)),headers=self.access_header, content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Entry has been created successfully", res.data)

    def test_to_create_entry_with_duplicate_data(self):
        """test to create an entry"""
        tester=self.app.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(title="Testing",
                body="testing data",user_id=1)),headers=self.access_header, content_type='application/json')
        self.assertEqual(res.status_code, 409)
        self.assertIn(b"Entry has been created previously,Duplicate data", res.data)
        
    def test_to_get_all_entries(self):
        """test to get all entries"""
        tester=self.app.test_client(self)
        response = tester.get('/API/v1/entries',headers=self.access_header,content_type="application/json")
        self.assertEqual(response.status_code, 200)
    
        def test_for_wrong_url(self):
            """test for wrong url"""
        tester=self.app.test_client(self)
        response = tester.get('/API/v1/iuut',
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_to_get_single_entry(self):
        """test to get a single entry content"""
        tester=self.app.test_client(self)
        response = tester.get('/API/v1/entries/1',headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_to_get_single_entry_with_invalid_id(self):
        """test to get a single entry content"""
        tester=self.app.test_client(self)
        response = tester.get('/API/v1/entries/11111',headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"The URL is invalid ,wrong ID given", response.data) 

    def test_to_update_entry(self):
        """test to get a single entry content"""
        tester=self.app.test_client(self)
        response = tester.put('/API/v1/entries/1',data=json.dumps(
            dict(title="war",
                body="We will be fine",user_id=1)),headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)