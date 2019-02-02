# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from products.models import product

# Create your models here.
class vendor_master(models.Model):
    Vendor_name = models.CharField(max_length=120)
    Vendor_Address = models.CharField(max_length=120)
    Vendor_mandi_name = models.CharField(max_length=120)
    loma_name = models.CharField(max_length=120)
    loma_zone = models.CharField(max_length=120)
    vendor_mobile_no = models.IntegerField(default = 0.00)
    #description = models.TextField(null=False)
    #price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)
    vendor_slug = models.SlugField(unique = True)
    #Image = models.FileField(upload_to='products/images/', null= True)   
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id


class vendor_daily_PL(models.Model):
    vendor = models.ForeignKey(vendor_master)
    product = models.ForeignKey(product)
    product_name = models.CharField(max_length=120, blank=True)
    offer_price = models.FloatField(null=False)
    list_price = models.IntegerField(null=False)
    qty = models.IntegerField(null=False)

    def __unicode__(self):
        return self.vendor_ID 

