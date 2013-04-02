# -*- coding: utf-8 -*-

import logging

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from django.test.client import Client


log = logging.getLogger(__name__)

test_admin_user = {
    'username': 'tester',
    'email': 'tester@test.com',
    'password': 'test'
}


class RCPilotLogTest(LiveServerTestCase):
    """Site-wide functional tests."""

    def setUp(self):
        User.objects.create_superuser(**test_admin_user)
        self.c = Client()

    def tearDown(self):
        u = User.objects.get(username=test_admin_user['username'],
                             email=test_admin_user['email'])
        u.delete()

    def test_basic_gets(self):
        resp = self.c.get('/admin/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("body", resp.content)
        self.assertIn("Django administration", resp.content)
