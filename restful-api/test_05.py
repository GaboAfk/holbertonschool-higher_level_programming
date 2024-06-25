#!/usr/bin/python3
import unittest
from task_05_basic_security import app, create_access_token
import base64
import json

class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_basic_auth_no_credentials(self):
        response = self.app.get('/basic-protected')
        self.assertEqual(response.status_code, 401)

    def test_login_valid_credentials(self):
        user = {"username": "user", "password": "user", "role": "user"}
        response = self.app.post('/login', data=json.dumps(user), content_type='application/json')
        acces_token = create_access_token(identity={"username": user["username"], "role": user["role"]})
        self.assertEqual(response.status_code, 200)
        self.assertIn(acces_token, response.json)


    """def test_jwt_protected(self):
        user = {"username": "user", "password": "user"}
        login_response = self.app.post("/login", json.dumps(user))
        token = login_response.json["access_token"]
        response = self.app.get("/jwt-protected", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "JWT Auth: Access Granted"})"""

if __name__ == '__main__':
    unittest.main()