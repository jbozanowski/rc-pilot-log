# -*- coding: utf-8 -*-

import logging

from model_utils import Choices
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from rcpilotlog.batteries.models import Battery
from rcpilotlog.rcmodels.models import RCModel


log = logging.getLogger(__name__)


class EventType(TimeStampedModel):
    name = models.CharField(_(u"name"), max_length=255)
    description = models.TextField(_(u"description"), blank=True)

    class Meta:
        verbose_name = _(u"Event Type")
        verbose_name_plural = _(u"Event Types")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Event(TimeStampedModel):
    event_type = models.ForeignKey(EventType, verbose_name=_(u"event type"))
    description = models.TextField(_(u"name"), blank=True)
    user = models.ForeignKey(User, verbose_name=_(u"user"))
    rcmodel = models.ForeignKey(RCModel, verbose_name=_(u"RC model"),
                                null=True, blank=True)
    battery = models.ForeignKey(Battery, verbose_name=_(u"battery"), null=True,
                                blank=True)
    duration = models.IntegerField(_(u"duration"), null=True, blank=True)
    description = models.TextField(_(u"description"), blank=True)

    class Meta:
        verbose_name = _(u"Event")
        verbose_name_plural = _(u"Events")
        ordering = ("user", "-created")

    def __unicode__(self):
        # FIXME
        return u"%s (%s @ %s)" % (
            self.get_event_type_display(),
            self.user,
            self.created
        )
