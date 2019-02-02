# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
import hashlib
# Create your models here.


class register_model(models.Model):
    firstname = models.CharField(max_length=250, help_text='Required')
    lastname = models.CharField(max_length=250, help_text='Required')
    username = models.CharField(max_length=250, help_text='Required')
    email = models.EmailField(max_length=250, help_text='Required')
    contact_no = models.IntegerField(null=True)
    slug = models.SlugField(unique = True, null=True)
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False) 
    email_verified = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    


    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['firstname','lastname']

    '''def get_absolute_url(self):
        return reverse('details', kwargs={'pk':self.pk})'''

    def __str__(self):
        return self.email

class address(models.Model):
    user = models.ForeignKey(register_model)
    city = models.CharField(max_length=30)
    service_area = models.CharField(max_length=100)
    local_address = models.CharField(max_length=200)
    pin = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return 'Address of %s' %(self.user.firstname)


