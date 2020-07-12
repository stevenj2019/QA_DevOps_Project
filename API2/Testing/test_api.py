from api import app
import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_multi(self):
        response= int(self.client.get('/get/multi').get_json()['multiply'])
        assert response >= 0 and response <= 5
        

        assert dictionary[key] >= 0 and dictionary[key] <= 10