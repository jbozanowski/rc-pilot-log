# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import RCModelType, RCModel


class RCModelTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class RCModelAdmin(admin.ModelAdmin):
    list_display = ("name", "rcmodel_type", "manufacturer", "owner")
    ordering = ("owner", "rcmodel_type", "name")


admin.site.register(RCModelType, RCModelTypeAdmin)
admin.site.register(RCModel, RCModelAdmin)
