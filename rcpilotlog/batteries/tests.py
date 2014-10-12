# -*- coding: utf-8 -*-

import copy
import logging

from django.contrib.auth.models import User
from django.test import TestCase

from rcpilotlog.functional_tests.tests import test_user

from .models import Battery


log = logging.getLogger(__name__)

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
        """Object creation and basic sanity check."""

        battery_data = copy.deepcopy(test_battery)
        battery_data.update({'owner': self.user})
        battery = Battery.objects.create(**battery_data)
        self.assertTrue(battery)
        self.assertTrue(all((repr(battery), str(battery))))
