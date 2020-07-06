import requests
from api import app
import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    #def test_slot(self):
        #opts = ['coin', 'clover', '7', 'horseshoe']
        #for i in range(0, 4):
            #with patch('random.randint') as r:
                #r.return_value = int(i)
                #self.assertEqual(slot(), opts[i])
        
    def test_machine(self):
        #with patch('api.slot') as s: 
            #s.return_value = ['coin', 'coin', 'coin']

        response = requests.get('http://localhost:5000/get/slot')
        self.assertEqual(s.return_value, response['machine'])
