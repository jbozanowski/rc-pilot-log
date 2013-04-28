# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import EventType, Event


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class EventAdmin(admin.ModelAdmin):
    list_display = ("user", "event_type", "rcmodel", "battery", "description")


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
