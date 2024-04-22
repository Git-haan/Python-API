import unittest
from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_hello_post(self):
        response = self.app.post('/hello', json={'name': 'World'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'name': 'World'})

    def test_hello_name(self):
        response = self.app.get('/hello/World')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_hello_name_post(self):
        response = self.app.post('/hello/World', json={'name': 'World'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'name': 'World'})

if __name__ == '__main__':
    unittest.main()
