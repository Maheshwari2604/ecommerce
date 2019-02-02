# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products.models import product, product_Image, product_price
from django.db import models

# Create your models here.
class cartitem(models.Model):
    cart = models.ForeignKey('Carttotal', null=True, blank=True)
    product = models.ForeignKey(product, null=True, blank=True)
    productImage = models.ForeignKey(product_Image, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    sub_total = models.DecimalField(default=19.99, max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title


class carttotal(models.Model):
    Total = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "cart id: %s" %(self.id)