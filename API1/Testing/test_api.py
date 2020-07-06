from api import app
import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_machine(self):
        answers = ['coin', 'clover', '7', 'horseshoe']
        response = self.client.get('/get/slot').get_json()
        assert response['machine'][0] in answers
