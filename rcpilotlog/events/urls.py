# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import listing


urlpatterns = patterns('',
    url(r'^$', listing, name='listing'),
)
