# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Battery


class BatteryAdmin(admin.ModelAdmin):
    list_display = ("name", "chemistry", "capacity", "manufacturer", "owner")
    ordering = ("owner", "chemistry", "name")


admin.site.register(Battery, BatteryAdmin)
