# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase

from rcpilotlog.functional_tests.tests import test_user

from .models import Battery


test_battery = {
    'name': 'Test Battery',
    # 'owner' needs a user created first,
    'manufacturer': 'Test Battery Manufacturer',
    'capacity': 2200,
    'chemistry': Battery.CHEMISTRY.lipo,
}


class BatteryTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**test_user)

    def test_object_creation(self):
        """Object creation sanity check."""

        test_battery.update({'owner': self.user})
        battery = Battery.objects.create(**test_battery)
        self.assertTrue(battery)
