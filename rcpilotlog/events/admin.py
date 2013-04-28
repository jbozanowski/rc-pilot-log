# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("user", "event_type", "rcmodel", "battery", "description")


admin.site.register(Event, EventAdmin)
