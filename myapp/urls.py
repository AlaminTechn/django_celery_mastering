from django.urls import path
from myapp.views import index , about , contact

urlpatterns = [
    path('', index , name='home'),
    path('about', about , name='about'),
    path('contact', contact , name='contact'),
]