from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from services.models import Service


# Create your views here.
def get_home_page(request):
  services = Service.objects.all()
  return render(request, 'home.html', {'services': services})
