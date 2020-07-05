from code.API1 import app
from flask import url_for
from flask_testing import TestCase
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_calc(self):
        response = requests.post('http://api:5000/get/calc', json={'win':25, 'multi':3})
        self.assertIn(b'75', response)