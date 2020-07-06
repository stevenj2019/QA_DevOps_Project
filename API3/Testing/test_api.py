from api import app
import unittest
from flask import url_for, jsonify
from flask_testing import TestCase
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_api(self):
        response = self.client.post('/get/total', json={'slot':25, 'multiple':3}).get_json()['TOTAL']
        assert response == 75