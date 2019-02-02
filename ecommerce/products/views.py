# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import product
from django.shortcuts import render

# Create your views here.

def home(request):
    products = product.objects.all()
    
    context = {
        "products": products
    }

    return render(request, 'products/home.html', context)

