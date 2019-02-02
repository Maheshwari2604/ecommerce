# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import cartitem,  carttotal
from django.contrib import admin

# Register your models here.
admin.site.register(cartitem)

admin.site.register(carttotal)