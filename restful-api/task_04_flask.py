import unittest
import json
from task_04_flask import app


class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Welcome to the Flask API!')

    def test_data_route(self):
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_status_route(self):
        response = self.client.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'OK')

    def test_get_user(self):
        response = self.client.get('/users/john')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['username'], 'john')

    def test_get_nonexistent_user(self):
        response = self.client.get('/users/nonexistent')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'User not found')

    def test_add_user(self):
        new_user_data = {
            'username': 'alice',
            'name': 'Alice',
            'age': 25,
            'city': 'San Francisco'
        }
        response = self.client.post('/add_user', json=new_user_data)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User added')
        self.assertEqual(data['user']['username'], 'alice')

    def test_add_user_no_username(self):
        new_user_data = {
            'name': 'Alice',
            'age': 25,
            'city': 'San Francisco'
        }
        response = self.client.post('/add_user', json=new_user_data)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Username is required')

    def test_add_duplicate_user(self):
        new_user_data = {
            'username': 'john',
            'name': 'John',
            'age': 30,
            'city': 'New York'
        }
        response = self.client.post('/add_user', json=new_user_data)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'User already exists')


if __name__ == '__main__':
    unittest.main()
