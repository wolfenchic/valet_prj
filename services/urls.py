from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', get_services_page, name='services'), 
    ]