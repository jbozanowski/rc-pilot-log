# -*- coding: utf-8 -*-

import logging

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from django.test.client import Client

from rcpilotlog.batteries.models import Battery
from rcpilotlog.events.models import Event
from rcpilotlog.rcmodels.models import RCModel


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

test_battery = {
    'name': 'Test Battery',
    # 'owner' needs a user created first,
    'manufacturer': 'Test Battery Manufacturer',
    'capacity': 2200,
    'chemistry': Battery.CHEMISTRY.lipo,
}

test_rcmodel = {
    'name': 'Test RC Model',
    'rcmodel_type': RCModel.MODEL_TYPES.heli,
    # 'owner' needs a user created first,
    'manufacturer': 'Test RC Model Manufacturer',
}

test_event = {
    'event_type': Event.EVENT_TYPES.flight,
    # 'user' needs a user created first,
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
        self.assertEqual(resp.status_code, 200)
        self.assertIn("body", resp.content)
        self.assertIn("Django administration", resp.content)
        resp = self.c.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("body", resp.content)
        self.assertIn("<title>", resp.content)

    def test_creating_objects(self):
        """Make sure we can actually create all of application's models."""

        test_battery.update({'owner': self.user})
        test_rcmodel.update({'owner': self.user})
        test_event.update({'user': self.user})

        battery = Battery.objects.create(**test_battery)
        rcmodel = RCModel.objects.create(**test_rcmodel)
        event = Event.objects.create(**test_event)
