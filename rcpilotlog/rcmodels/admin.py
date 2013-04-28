# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import RCModel


class RCModelAdmin(admin.ModelAdmin):
    list_display = ("name", "rcmodel_type", "manufacturer", "owner")
    ordering = ("owner", "rcmodel_type", "name")


admin.site.register(RCModel, RCModelAdmin)
