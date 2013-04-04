# -*- coding: utf-8 -*-

import logging

from model_utils.models import TimeStampedModel

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


log = logging.getLogger(__name__)


class RCModelType(TimeStampedModel):
    name = models.CharField(_(u"name"), max_length=255)
    description = models.TextField(_(u"description"))
    # TODO:
    # - thumbnail (find a good thumbnail library)

    class Meta:
        verbose_name = _(u"RC Model Type")
        verbose_name_plural = _(u"RC Model Types")
        ordering = ["name"]


class RCModel(TimeStampedModel):
    name = models.CharField(_(u"name"), max_length=255)
    rcmodel_type = models.ForeignKey(RCModelType,
        verbose_name=_(u"Your RC Model's Type"))
    owner = models.ForeignKey(User, verbose_name=_(u"Owner"))
    manufacturer = models.CharField(_(u"manufacturer"), max_length=255)
    description = models.TextField(_(u"description"))
    # TODO:
    # - pics (find a good pic/thumbnail library, etc.)
    #   - a gallery? probably much later, if ever

    class Meta:
        verbose_name = _(u"RC Model")
        verbose_name_plural = _(u"RC Models")
