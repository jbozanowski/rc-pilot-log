# -*- coding: utf-8 -*-

import copy
import logging

from django.contrib.auth.models import User
from django.test import TestCase

from rcpilotlog.functional_tests.tests import test_user

from .models import Event


log = logging.getLogger(__name__)

test_event = {
    'event_type': Event.EVENT_TYPES.flight,
    # 'user' needs a user created first,
}


class EventTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**test_user)

    def test_object_creation(self):
        """Object creation sanity check."""

        event_data = copy.deepcopy(test_event)
        event_data.update({'user': self.user})
        event = Event.objects.create(**event_data)
        self.assertTrue(event)
        self.assertTrue(all((repr(event), str(event))))
