# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase

from rcpilotlog.functional_tests.tests import test_user

from .models import Event


test_event = {
    'event_type': Event.EVENT_TYPES.flight,
    # 'user' needs a user created first,
}


class EventTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**test_user)

    def test_object_creation(self):
        """Object creation sanity check."""

        test_event.update({'user': self.user})
        event = Event.objects.create(**test_event)
        self.assertTrue(event)
