import unittest
from unittest.mock import patch

from flask import url_for, request
from flask_testing import TestCase
from flask_login import login_user, current_user, logout_user
import requests

from Application import app, db, crypt
from Application.models import User
from os import getenv

def user_login(self):
    response = self.client.post(
            '/login',
            data=dict(
                email='sjo739273@mail.com', 
                password='9797ifdhvsd'
            ),
        follow_redirects=True
        )
    return response

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        self.user = User(email='sjo739273@mail.com', password=crypt.generate_password_hash('9797ifdhvsd'), balance=10)

        db.session.add(self.user)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
class TestRoutes(TestBase):
    def test_login(self):
        self.assertIn(self.client.get(url_for('login')), 200)
        self.assertIn(self.client.post(
            '/login',
            data=dict(
                email='sjo739273@mail.com', 
                password='9797ifdhvsd'
            ),
        follow_redirects=True
        ).response_code, 200)

    def test_register(self):
        self.assertEqual(self.client.get(url_for('register')).status_code, 200)
        self.assertIn(b'email@test.uk', self.client.post('/register', data=dict(email='email@test.uk', password='thispasswordsucks'), follow_redirects=True).data)

    def test_login(self):
        self.assertEqual(self.client.get(url_for('login')).status_code, 200)
        with self.client:
            user_login(self)
            self.assertRedirects(self.client.get(url_for('login')), url_for('home'))

    def test_logout(self):
        with self.client:
            user_login(self)
            self.assertRedirects(self.client.get(url_for('logout')), url_for('login'))

    def test_home(self):
        self.assertRedirects(self.client.get(url_for('home')), str(url_for('login')+'?next=%2Fhome'))
        user_login(self)
        self.assertEqual(self.client.get(url_for('home')).status_code, 200)

    def test_topup(self):
        self.assertRedirects(self.client.get(url_for('topup')), url_for('login')+'?next=%2Ftopup')
        with self.client:
            user_login(self)
            self.assertEqual(self.client.get(url_for('topup')).status_code, 200)
            self.assertIn(b'5', self.client.post('/topup', data=dict(cash=5), follow_redirects=True).data)

    def test_slots(self):
        self.assertRedirects(self.client.get(url_for('slots')), url_for('login')+'?next=%2Fslots')
        with self.client:
            user_login(self)
            with patch('requests.get') as 1:
                p.return_value=['coin', 'coin', 'coin']
            with patch()

    def test_delete(self):
        with self.client:
            user_login(self)
            self.assertRedirects(self.client.get(url_for('delete')), url_for('register'))