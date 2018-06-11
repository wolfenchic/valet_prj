from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.http import HttpResponse
from .models import Service
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import auth, messages



# Create your views here.

def get_services_page(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})
    

def get_vouchers_page(request):
    services = Service.objects.all()
    return render(request, 'vouchers.html', {'services': services})

