# -*- coding: utf-8 -*-

import logging

from model_utils import Choices
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


log = logging.getLogger(__name__)


class Battery(TimeStampedModel):
    CHEMISTRY = Choices(
        ('lipo', _(u"Lithium Polymer (LiPo)")),
        ('liion', _(u"Lithium-ion (Li-Ion)")),
        ('nicd', _(u"Nickel Cadmium (NiCd)")),
    )

    name = models.CharField(_(u"name"), max_length=255)
    owner = models.ForeignKey(User, verbose_name=_(u"Owner"))
    manufacturer = models.CharField(_(u"manufacturer"), max_length=255)
    capacity = models.PositiveIntegerField(_(u"capacity (in mAh)"))
    chemistry = models.CharField(_(u"chemistry"), choices=CHEMISTRY,
                                 default=CHEMISTRY.lipo, max_length=128)
    description = models.TextField(_(u"description"), blank=True)

    class Meta:
        verbose_name = _(u"Battery")
        verbose_name_plural = _(u"Batteries")
        ordering = ['owner', 'name']

    def __str__(self):
        return "{name} ({manufacturer} {chemistry}, {capacity}" \
               " mAh".format(
                    name=self.name,
                    manufacturer=self.manufacturer,
                    chemistry=self.chemistry,
                    capacity=self.capacity
               )
