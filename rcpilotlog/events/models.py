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


class Event(TimeStampedModel):
    EVENT_TYPES = Choices(
        ('flight', _(u"Flight")),
        ('batt_charge', _(u"Battery charge")),
        ('batt_discharge', _(u"Battery discharge")),
        ('crash', _(u"Model crash")),
        ('maintenance', _(u"Craft maintenance")),
    )

    event_type = models.CharField(_(u"event type"), choices=EVENT_TYPES,
                                  default=EVENT_TYPES.flight, max_length=128)
    description = models.TextField(_(u"name"), blank=True)
    user = models.ForeignKey(User, verbose_name=_(u"user"))
    rcmodel = models.ForeignKey(RCModel, verbose_name=_(u"RC model"),
                                null=True, blank=True)
    battery = models.ForeignKey(Battery, verbose_name=_(u"battery"), null=True,
                                blank=True)
    duration = models.IntegerField(_(u"duration"), null=True, blank=True)
    capacity_charged = models.PositiveIntegerField(
        _(u"capacity charged (in mAh)"), null=True, blank=True)
    description = models.TextField(_(u"description"), blank=True)

    class Meta:
        verbose_name = _(u"Event")
        verbose_name_plural = _(u"Events")
        ordering = ("user", "-created")

    def __str__(self):
        return "{event_type} ({user} @ {created})".format(
            event_type=self.get_event_type_display(),
            user=self.user,
            created=self.created
        )
