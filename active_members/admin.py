# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(BdeSecurityGroup, InsaSecurityGroup, LedMailing)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','type','responsable','nombre')
    list_filter = ('type',)
    ordering = ('name',)
    search_fields = ('name',)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "resp_mailing":
            kwargs["queryset"] = LedMailing.objects.filter(type="R")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(SubTeam)
class SubTeamAdmin(admin.ModelAdmin):
    list_display = ('name','team', 'responsable', 'nombre')
    list_filter = ('team',)
    ordering = ('team','name',)
    search_fields = ('name',)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "mailing":
            kwargs["queryset"] = LedMailing.objects.filter(type="S")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'promo', 'is_ma', 'profil_complete')
    ordering=('-first_name',)
