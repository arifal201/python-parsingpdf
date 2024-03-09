from django.urls import path
from . import views

urlpatterns = [
  path('home', views.home, name='homepage'),
  path('servicepdf/parsing-pc135', views.parsingpdf, name='parsingpdf'),
]