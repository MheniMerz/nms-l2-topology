import unittest
import os

class testConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.auth_1 = {'username':'admin', 'password':'admin'}
        self.auth_2 = {'username':'random', 'password':'shouldFail'}
        
        self.api_client_1 = apiClient(url_base=str(os.environ.get('API_SERVER_URL')),
                                        auth=self.auth_1)
        self.api_client_2 = apiClient(url_base=str(os.environ.get('API_SERVER_URL')),
                                        auth=self.auth_2)

    def tearDown(self):
        self.api_client = None
        self.auth_1 = None
        self.auth_2 = None

    def test_read_config(self):
        self.assertEqual(self.auth_1.login(self.api_client), '201')
        self.assertEqual(self.auth_2.login(self.api_client), '401')

if __name__ == '__main__':
    unittest.main()
