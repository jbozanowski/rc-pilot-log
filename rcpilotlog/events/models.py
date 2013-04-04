# -*- coding: utf-8 -*-

import logging

from model_utils import Choices
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


log = logging.getLogger(__name__)


class EventType(TimeStampedModel):
    name = models.CharField(_(u"name"), max_length=255)
    description = models.TextField(_(u"description"))

    class Meta:
        verbose_name = _(u"Event Type")
        verbose_name_plural = _(u"Event Types")
        ordering = ['name']


class Event(TimeStampedModel):
    pass

    class Meta:
        pass
