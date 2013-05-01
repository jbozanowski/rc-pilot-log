# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy as reverse_l


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'rcpilotlog.main.views.main_page', name="main-page"),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': "main/login.html"},
        name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': reverse_l('main-page')},
        name="logout"),

    url(r'^events/', include('rcpilotlog.events.urls', namespace='events')),
)
