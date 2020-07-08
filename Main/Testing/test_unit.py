import unittest

from flask import url_for
from flask_testing import TestCase

from Application import app, db
from Application.models import User
from os import getenv

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

        user = User(email='sjo739273@mail.com', balance=5)

        db.sessions.add(user)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    #def login(self):

    #def logout(self):


class TestView(TestBase):
    #def test_auth(self):
        #testing redirection

    def test_register(self):
        self.assertEqual(self.client.get(url_for('register')).status_code, 200)
        #test POST function also 

    def test_login(self):
        self.assertEqual(self.client.get(url_for('login')).status_code, 200)
        #test POST function also

    def test_main(self):
        #find out how to test for redirections
        #self.login()
        self.assertEqual(self.client.get(url_for('home')).status_code, 200)
        #self.logout()

    def test_topup(self):
        #find out how to test for redirections
        #self.login()
        self.assertEqual(self.client.get(url_for('topup')).status_code, 200)
        #self.logout()
        
    def test_main(self):
        self.assertEqual(self.client.get(url_for('slots')).status_code, 200)

class TestFunction(TestBase):
    def test_auth(self):
        self.assertIn(b'sjo7382927@mail.com', self.client.post('/', data = dict(email_address = 'sjo7382927@mail.com')))