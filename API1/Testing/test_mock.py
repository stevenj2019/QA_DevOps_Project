from code.API1 import app
from code.API1 import slot
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_slot(self):
        opts = ['coin', 'clover', '7', 'horseshoe']
        for i in range(0, 4):
            with patch('random.randint') as r:
                r.return_value = i
                self.assertEqual(slot(), opts[i])
        
    def test_machine(self):
        with patch('slot') as s: 
            s.return_value = ['coin', 'coin', 'coin']

            response = self.client.get(url_for('machine'))
            self.assertEqual(s.return_value, response)
