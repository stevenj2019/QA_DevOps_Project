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
        assert self.client.post('/get/total', json={'slot':['coin', 'coin', '7'], 'multiple':3}).get_json()['TOTAL'] == 300
        assert self.client.post('/get/total', json={'slot':['coin', 'coin', 'coin'], 'multiple':3}).get_json()['TOTAL'] == 450
        assert self.client.post('/get/total', json={'slot':['clover', 'horseshoe', 'clover'], 'multiple':2}).get_json()['TOTAL'] == 100
        assert self.client.post('/get/total', json={'slot':['7', '7', 'clover'], 'multiple':4}).get_json()['TOTAL'] == 80
        assert self.client.post('/get/total', json={'slot':['clover', 'horseshoe', 'horseshoe'], 'multiple':2}).get_json()['TOTAL'] == 20
        assert self.client.post('/get/total', json={'slot':['clover', 'horseshoe', '7'], 'multiple':2}).get_json()['TOTAL'] == 0