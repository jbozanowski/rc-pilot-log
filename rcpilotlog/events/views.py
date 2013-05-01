# -*- coding: utf-8 -*-

import logging

from django.template import RequestContext
from django.template.response import TemplateResponse


log = logging.getLogger(__name__)


def listing(request):
    context = RequestContext(request, {})
    return TemplateResponse(request, 'events/listing.html', context)
