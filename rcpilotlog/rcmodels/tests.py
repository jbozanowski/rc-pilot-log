# -*- coding: utf-8 -*-

import copy
import logging

from django.contrib.auth.models import User
from django.test import TestCase

from rcpilotlog.functional_tests.tests import test_user

from .models import RCModel


log = logging.getLogger(__name__)

test_rcmodel = {
    'name': 'Test RC Model',
    'rcmodel_type': RCModel.MODEL_TYPES.heli,
    # 'owner' needs a user created first,
    'manufacturer': 'Test RC Model Manufacturer',
}


class RCModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**test_user)

    def test_object_creaion(self):
        """Object creation sanity check."""

        rcmodel_data = copy.deepcopy(test_rcmodel)
        rcmodel_data.update({'owner': self.user})
        rcmodel = RCModel.objects.create(**rcmodel_data)
        self.assertTrue(rcmodel)
        self.assertTrue(all((repr(rcmodel), str(rcmodel))))
