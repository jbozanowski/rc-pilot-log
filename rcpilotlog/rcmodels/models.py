# -*- coding: utf-8 -*-

import logging

from model_utils import Choices
from model_utils.models import TimeStampedModel

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


log = logging.getLogger(__name__)


class RCModel(TimeStampedModel):
    MODEL_TYPES = Choices(
        ('heli', _(u"Helicopter")),
        ('multicopter', _(u"Multicopter")),
        ('acro', _(u"Airplane")),
        ('glider', _(u"Glider")),
        ('motoglider', _(u"Motor Glider")),
    )

    name = models.CharField(_(u"name"), max_length=255)
    rcmodel_type = models.CharField(_(u"Your RC Model's Type"),
                                    choices=MODEL_TYPES,
                                    default=MODEL_TYPES.heli, max_length=64)
    owner = models.ForeignKey(User, verbose_name=_(u"Owner"))
    manufacturer = models.CharField(_(u"manufacturer"), max_length=255)
    description = models.TextField(_(u"description"), blank=True)
    # TODO:
    # - pics (find a good pic/thumbnail library, etc.)
    #   - a gallery? probably much later, if ever

    class Meta:
        verbose_name = _(u"RC Model")
        verbose_name_plural = _(u"RC Models")

    def __unicode__(self):
        return self.name
