# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=False)
    #price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)
    slug = models.SlugField(unique = True)
    #Image = models.FileField(upload_to='products/images/', null= True)   
    #timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class product_Image(models.Model):
    Product = models.ForeignKey(product)
    image = models.ImageField(upload_to='products/images/', blank=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    #active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.Product.title   

class product_price(models.Model):
    product = models.ForeignKey(product)
    product_Image = models.ForeignKey(product_Image)
    #product_offer = models.ForeignKey(product_discount)
    price = models.PositiveIntegerField(default = 0.00)
    lastupdated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.product.title

class product_discount(models.Model):
    product = models.ForeignKey(product)
    Offer = models.IntegerField(default = 0.00)
    lastupdated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.product.title


class Daily_price_list(models.Model):
    price_list_date = models.DateField(auto_now_add=True)
    price_list_time = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(product)
    vendor_id = models.CharField(default=101, max_length=30)
    offer_price = models.FloatField(default=10.5)
    list_price = models.IntegerField(default=0.00)
    margin = models.FloatField(default=0.00)
    total_available_quantity = models.FloatField(default=50.5)
    rating = models.IntegerField(default=2.5)
    #Total = models.FloatField(default=0.00) ('ye alag table hogi total ke liye')

    def __unicode__(self):
        return self.product.title
