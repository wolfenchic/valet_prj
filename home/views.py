from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from services.models import Service
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import auth, messages


# Create your views here.
def get_home_page(request):
  services = Service.objects.all()
  return render(request, 'home.html', {'services': services})

