# -*- coding: utf-8 -*-

import logging

from django.template import RequestContext
from django.template.response import TemplateResponse


log = logging.getLogger(__name__)


def main_page(request):
    context = RequestContext(request, {
    })
    return TemplateResponse(request, 'main/main_page.html', context)
