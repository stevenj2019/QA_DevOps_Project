from Code.API2 import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_multi(self):
        with patch('multi') as m: 
            m.return_value.text = '2'

            response = self.client.get(url_for('multi'))
            self.assertIn(b'2', response)