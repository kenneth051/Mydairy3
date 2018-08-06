"""API test page"""
from app.tests.test_basefile import TestBase


class EntryTesting(TestBase):
    """class to test our entries"""

    def test_to_create_entry(self):
        """test to create an entry"""
        tester = self.app.test_client(self)
        res = tester.post('/API/v1/entries', data=TestBase.create_entry,
                          headers=self.access_header,
                          content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Entry created successfully", res.data)

    def test_to_create__duplicate_entry(self):
        """test to create an entry with duplicate data"""
        tester = self.app.test_client(self)
        res = tester.post('/API/v1/entries', data=TestBase.duplicate_entry,
                          headers=self.access_header,
                          content_type='application/json')
        self.assertEqual(res.status_code, 409)
        self.assertIn(b"Duplicate Entry data",
                      res.data)

    def test_to_get_all_entries(self):
        """test to get all entries"""
        tester = self.app.test_client(self)
        response = tester.get('/API/v1/entries', headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_to_get_single_entry(self):
        """test to get a single entry content"""
        tester = self.app.test_client(self)
        response = tester.get('/API/v1/entries/1', headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_to_get_invalid_entry(self):
        """test to get an entry with invalid id"""
        tester = self.app.test_client(self)
        response = tester.get('/API/v1/entries/11111',
                              headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"The Page cannot be found", response.data)

    def test_duplicate_update(self):
        """test to update an entry using duplicate data"""
        tester = self.app.test_client(self)
        response = tester.put('/API/v1/entries/1',
                              data=TestBase.duplicate_update,
                              headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 409)

    def test_to_update_entry(self):
        """test to update an entry"""
        tester = self.app.test_client(self)
        response = tester.put('/API/v1/entries/1', data=TestBase.update_entry,
                              headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_to_update_invalid_entry(self):
        """test to get an entry with invalid id"""
        tester = self.app.test_client(self)
        response = tester.put('/API/v1/entries/11111', data=TestBase.update_entry,
                              headers=self.access_header,
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"The Page cannot be found", response.data)    
