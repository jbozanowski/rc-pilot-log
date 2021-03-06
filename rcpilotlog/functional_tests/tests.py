# -*- coding: utf-8 -*-

import logging

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from django.test.client import Client


log = logging.getLogger(__name__)

test_admin_user = {
    'username': 'admin_tester',
    'email': 'admin_tester@test.com',
    'password': 'test'
}

test_user = {
    'username': 'tester',
    'email': 'tester@test.com',
    'password': 'test'
}


class RCPilotLogTest(LiveServerTestCase):
    """Site-wide functional tests."""

    def setUp(self):
        self.user = User.objects.create_user(**test_user)
        self.admin_user = User.objects.create_superuser(**test_admin_user)
        self.c = Client()

    def tearDown(self):
        self.user.delete()
        self.admin_user.delete()

    def test_basic_gets(self):
        resp = self.c.get('/admin/')
        self.assertEqual(resp.status_code, 302)

        resp = self.c.get('/admin/', follow=True)
        self.assertEqual(resp.status_code, 200)

        resp = self.c.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        resp = self.c.get(reverse('logout'))
        self.assertEqual(resp.status_code, 302)

        resp = self.c.get(reverse('main-page'))
        self.assertContains(resp, "<body>", status_code=200)
        
        resp = self.c.get(reverse('events:listing'))
        self.assertContains(resp, "<body>", status_code=200)

    def test_logged_in_gets(self):
        resp = self.c.post('/login/', {'username': test_admin_user['username'],
                                       'password': test_admin_user['password']})
        self.assertTrue(resp.status_code, 200)

        resp = self.c.get('/admin/')
        self.assertContains(resp, "<body", status_code=200)
        self.assertContains(resp, "Django site admin")
