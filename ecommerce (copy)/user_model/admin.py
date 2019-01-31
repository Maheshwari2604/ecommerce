# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import register_model
from django.contrib import admin

# Register your models here.

class register(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'username' ,'email', 'timestamp', 'updated', 'is_active']
    list_editable = ['is_active']
    search_fields = ['username', 'email']
    date_hierarchy = 'timestamp'
    readonly_fields = ['timestamp', 'updated']
    prepopulated_fields = {"slug": ("username",)}

    class meta:
        model = register_model

admin.site.register(register_model, register)
